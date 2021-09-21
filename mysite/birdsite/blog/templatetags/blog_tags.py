from django import template
from ..models import Bird
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.simple_tag
def total_birds():
    return Bird.objects.count()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
