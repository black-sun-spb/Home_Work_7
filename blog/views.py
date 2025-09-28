from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import BlogPost
from django.conf import settings

# Миксин для проверки, что пользователь — контент-менеджер
class ContentManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name="Контент-менеджер").exists()

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

        if obj.views_count == 100:
            send_mail(
                "Статья набрала 100 просмотров!",
                f"Поздравляем! Статья «{obj.title}» достигла 100 просмотров.",
                settings.DEFAULT_FROM_EMAIL,
                ["taisiya199264@gmail.com"],
                fail_silently=False,
            )
        return obj

# Создание статьи — только для контент-менеджеров
class BlogCreateView(LoginRequiredMixin, ContentManagerRequiredMixin, CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogpost_form.html"

# Редактирование статьи — только для контент-менеджеров
class BlogUpdateView(LoginRequiredMixin, ContentManagerRequiredMixin, UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blogpost_form.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

# Удаление статьи — только для контент-менеджеров
class BlogDeleteView(LoginRequiredMixin, ContentManagerRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
