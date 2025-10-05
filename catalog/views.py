from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Product, Contact, Category
from .forms import ProductForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from .services import get_products_by_category
from django.core.cache import cache
from django.contrib.auth.decorators import permission_required
from django.conf import settings


# Главная страница — общедоступна
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 6

    def get_queryset(self):
        if getattr(settings, "CACHE_ENABLED", False):
            products = cache.get('all_products')
            if not products:
                products = Product.objects.filter(status="published").order_by('-created_at')
                cache.set('all_products', products, 60 * 5)
        else:
            products = Product.objects.filter(status="published").order_by('-created_at')
        return products


# Страница контактов — общедоступна
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context


# Детали товара — общедоступны
@method_decorator(cache_page(60 * 5), name='dispatch')  # кэш на 5 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# Добавление товара — только для авторизованных
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # ✅ назначаем владельца
        return super().form_valid(form)


# Редактирование товара — только для владельца
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/edit_product.html'
    login_url = 'users:login'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner  # ✅ редактировать может только владелец


# Удаление товара — владелец или модератор
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        # ✅ удалять может владелец или модератор (имеющий право на удаление товара)
        return user == product.owner or user.has_perm("catalog.delete_product")

def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = get_products_by_category(category.id)
    return render(request, 'catalog/products_by_category.html', {
        'category': category,
        'products': products
    })

@permission_required('catalog.can_unpublish_product', raise_exception=True)
def publish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_published = True
    product.save()
    return redirect('catalog:product_detail', pk=pk)


@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_published = False
    product.save()
    return redirect('catalog:product_detail', pk=pk)