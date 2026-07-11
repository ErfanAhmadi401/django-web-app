from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_home, name="blog-home"),
    path("single/", views.blog_single, name="blog-single"),
    path("test/", views.test, name="test"),

]
