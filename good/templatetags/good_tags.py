from ..models import GoodCategory, GoodColor
from django import template

register = template.Library()


@register.inclusion_tag('good/categories.html')
def show_category():
    good_categories = GoodCategory.objects.all()
    return {'categories': good_categories}

@register.inclusion_tag('good/colors.html')
def show_color():
    good_colors = GoodColor.objects.all()
    return {'colors': good_colors}
