from django import template
from women import models

register = template.Library()

@register.simple_tag(name="get_cats")
def get_categories(filter=None):
    if not filter:
        return models.Category.objects.all()
    else:
        return models.Category.objects.filter(pk=filter)


@register.inclusion_tag("women/list_categories.html")
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = models.Category.objects.all()
    else:
        categories = models.Category.objects.order_by(sort)

    return {"categories":categories, "category_selected":category_selected}