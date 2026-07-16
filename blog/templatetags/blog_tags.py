from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name="totalposts")
def sum():
    posts_count = Post.objects.filter(status=1).count()
    return posts_count


@register.simple_tag(name="posts")
def sum():
    posts = Post.objects.filter(status=1)
    return posts