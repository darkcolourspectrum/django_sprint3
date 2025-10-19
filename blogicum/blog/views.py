from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    """Главная страница - показывает последние 5 опубликованных постов."""
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category', 'location', 'author')[:5]

    context = {
        'post_list': posts,
    }
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    """Страница категории - показывает все посты определённой категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category', 'location', 'author')

    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    """Страница отдельного поста."""
    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)
