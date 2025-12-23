from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

def get_published_posts():
    return Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )

def index(request):
    template = 'blog/index.html'
    post_list = get_published_posts()[:5]
    return render(request, template, {'post_list': post_list})

def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        id=id
    )
    return render(request, template, {'post': post})

def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related(
        'author', 'location'
    )

    return render(
        request,
        template,
        {'category': category, 'post_list': post_list}
    )

