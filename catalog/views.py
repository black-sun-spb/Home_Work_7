from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Product, Contact
from .forms import ProductForm


# Главная страница — общедоступна
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 6
    ordering = ['-created_at']


# Страница контактов — общедоступна
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context


# Детали товара — общедоступны
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
