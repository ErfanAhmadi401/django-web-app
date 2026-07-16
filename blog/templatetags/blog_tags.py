from django import template

register = template.Library()

@register.simple_tag
def function(a):
    return a + 2


@register.simple_tag(name="plus")
def sum(a):
    return a + 2


@register.simple_tag(name="default")
def mines(a=2):
    return a - 2