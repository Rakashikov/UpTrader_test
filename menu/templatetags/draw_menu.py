from django import template
from django.db.models import Q

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('template_tag/menu.html', takes_context=True)
def draw_menu(context, slug):
    menu_items = MenuItem.objects.filter(Q(menu__slug=slug) &
                                         (Q(parent=None) | Q(parent__slug=context['slug'])))
    return {'menu': menu_items.get(slug=context['slug']).menu.title, 'menu_items': menu_items}
