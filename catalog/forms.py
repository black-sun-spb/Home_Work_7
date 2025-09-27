from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# список запрещённых слов
FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]


class ContactForm(forms.Form):
    """Форма обратной связи"""
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap к каждому полю
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'description':
                field.widget.attrs['rows'] = 5

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название не может содержать запрещённое слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание не может содержать запрещённое слово: {word}")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверяем, что это загруженный файл
            if hasattr(image, 'content_type'):
                # Проверка формата
                if image.content_type not in ['image/jpeg', 'image/png']:
                    raise ValidationError("Разрешены только JPEG и PNG форматы.")
                # Проверка размера
                if image.size > 5 * 1024 * 1024:
                    raise ValidationError("Размер изображения не должен превышать 5 МБ.")
        return image
