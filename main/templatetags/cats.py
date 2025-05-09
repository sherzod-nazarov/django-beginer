from django import template
from main.models import Categorys


register = template.Library()


@register.simple_tag(name='categories')
def get_categories():
    return Categorys.objects.all()