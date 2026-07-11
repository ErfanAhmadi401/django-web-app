from django.shortcuts import render
from blog.models import Post


def blog_home(request):
    context = {
        "first_name":"Erfan",
        "last_name":"Ahmadi",
        
    }
    return render(request, "blog/blog-home.html", context)


def blog_single(request):
    return render(request, "blog/blog-single.html")


def test(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
        
    }
    return render(request, "test.html", context)