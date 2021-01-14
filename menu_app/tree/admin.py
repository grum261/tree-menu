from django.contrib import admin
from .models import Menu, MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_visible', )
    list_editable = ('is_visible', )
    list_filter = ('parent',)


admin.site.register(Menu)