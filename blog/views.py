from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_home(request):
    posts = Post.objects.all().filter(status=1)
    context = {
        "posts": posts,

    }
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    posts = Post.objects.all().filter(status=1)
    post = get_object_or_404(posts, id=pid)
    context = {
        "post": post,
        
    }
    return render(request, "blog/blog-single.html", context)


def test(request):
    return render(request, "test.html")

