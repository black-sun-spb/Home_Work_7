from django.shortcuts import render
from django.contrib import messages
from catalog.models import Product, Contact

# Главная страница
def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    print("Последние 5 продуктов:")
    for p in latest_products:
        print(p.name, p.created_at)

    return render(request, 'catalog/home.html', {'latest_products': latest_products})

# Страница контактов
def contacts(request):
    contacts = Contact.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь можно добавить логику отправки письма или сохранения в базу
        messages.success(request, f"Спасибо, {name}! Ваше сообщение отправлено.")

    return render(request, 'catalog/contacts.html', {'contacts': contacts})
