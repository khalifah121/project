from django import template
from course.models import Category

register = template.Library()

@register.inclusion_tag('menu.html')
def menu():
    categories = Category.objects.all()
    return{'categories': categories}