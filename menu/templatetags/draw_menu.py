from django import template

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('template_tag/menu.html', takes_context=True)
def draw_menu(context, slug):
    menu_items = MenuItem.objects.filter(menu__slug=slug)
    menu_title = menu_items.all()[:1].get().menu.title
    item = None
    try:
        if context['slug'] != "favicon.ico":
            item = menu_items.get(slug=context['slug'])
            if item.parent is not None:
                item = item.parent
            items = [x for x in menu_items if x.parent is None]
            items = items[items.index(item) + 1:]
            for i in items:
                menu_items = menu_items.exclude(parent__slug=i.slug)
            return {'menu': menu_title, 'menu_items': menu_items}
    except:
        return {'menu': menu_title, 'menu_items': menu_items.filter(parent=None)}
