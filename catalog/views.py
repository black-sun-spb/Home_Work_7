from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy, reverse
from .models import Product, Contact
from .forms import ProductForm

# Главная страница
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 6
    ordering = ['-created_at']


# Страница контактов
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context


# Детали товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# Добавление товара
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')


# Редактирование товара
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/edit_product.html'

    def get_success_url(self):
        # После успешного редактирования перенаправляем на страницу товара
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


# Удаление товара
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:home')
