from ..models import GoodCategory
from django import template

register = template.Library()


@register.inclusion_tag('good/categories.html')
def show_category():
    good_categories = GoodCategory.objects.all()
    return {'categories': good_categories}
