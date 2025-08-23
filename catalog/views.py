from django.shortcuts import render
from django.contrib import messages


# Главная страница
def home(request):
    return render(request, 'catalog/home.html')


# Страница контактов
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь можно добавить логику отправки письма или сохранения в базу
        messages.success(request, f"Спасибо, {name}! Ваше сообщение отправлено.")

    return render(request, 'catalog/contacts.html')
