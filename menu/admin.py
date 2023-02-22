from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemAdmin(admin.TabularInline):
    model = MenuItem
    fields = ('title', 'url', 'slug', 'parent')
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    fields = ('title',)
    inlines = [MenuItemAdmin]
    save_as = True


admin.site.register(Menu, MenuAdmin)
