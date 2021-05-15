from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blog(request):
    """ A view to show all blog posts """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, blog_id):
    """ A view to show individual blog posts """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
