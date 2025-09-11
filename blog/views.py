from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import BlogPost
from django.conf import settings


# Список статей (только опубликованные)
class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")


# Детали статьи (+ увеличиваем просмотры)
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()

        # Доп. задание: письмо при 100 просмотрах
        if obj.views_count == 100:
            send_mail(
                "Статья набрала 100 просмотров!",
                f"Поздравляем! Статья «{obj.title}» достигла 100 просмотров.",
                settings.DEFAULT_FROM_EMAIL,
                ["taisiya199264@gmail.com"],
                fail_silently=False,
            )
        return obj


# Создание статьи
class BlogCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogpost_form.html"


# Редактирование статьи (после редирект на детальный просмотр)
class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogpost_form.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


# Удаление статьи
class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blogpost_list")

