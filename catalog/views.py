from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product, Contact
from .forms import ProductForm


# Главная страница с пагинацией
def home(request):
    product_list = Product.objects.order_by('-created_at')
    paginator = Paginator(product_list, 6)  # по 6 товаров на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'page_obj': page_obj})


# Страница контактов
def contacts(request):
    contacts = Contact.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Тут можно добавить отправку письма
        messages.success(request, f"Спасибо, {name}! Ваше сообщение отправлено.")

    return render(request, 'catalog/contacts.html', {'contacts': contacts})


# Детали товара
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


# Добавление товара
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
