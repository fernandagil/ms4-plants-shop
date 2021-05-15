from django.shortcuts import render
from .models import Blog


def all_blog(request):
    """ A view to show all blog articles """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
