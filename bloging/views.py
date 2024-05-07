from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from bloging.models import Blog


class BlogListView(ListView):
    """
    Регистрация класса "Blog" из bloging/models.py в админ панель
    """
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """
        Переопределение метода "get_queryset" для фильтрации отзывов
        """
        queryset = super().get_queryset().order_by(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    """
    Регистрация класса "Blog" из bloging/models.py в админ панель
    """
    model = Blog
    fields = ('title', 'body', 'image',)
    success_url = reverse_lazy('bloging:list')

    def form_valid(self, form):
        """
        Переопределение метода "form_valid" для сохранения слага
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """
    Класс для редактирования отзыва
    """
    model = Blog
    fields = ('title', 'body', 'image',)

    def form_valid(self, form):
        """
        Переопределение метода "form_valid" для сохранения слага
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        """
        Переопределение метода "get_success_url" для перехода на страницу отзыва
        """
        return reverse('bloging:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """
    Регистрация класса "Blog" из bloging/models.py в админ панель
    """
    model = Blog
    success_url = reverse_lazy('bloging:list')


def publication(request, pk):
    """
    Функция для публикации отзыва
    """
    publication_item = get_object_or_404(Blog, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True
    publication_item.save()
    return redirect(reverse('bloging:list'))
