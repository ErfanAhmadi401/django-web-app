from django.shortcuts import render


def blog_home(request):
    context = {
        "first_name":"Erfan",
        "last_name":"Ahmadi",
        
    }
    return render(request, "blog/blog-home.html", context)


def blog_single(request):
    return render(request, "blog/blog-single.html")
