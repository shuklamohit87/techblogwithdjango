from django.contrib import admin
from submenu.models import SubMenu
# Register your models here.
class SubMenuAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(SubMenu,SubMenuAdmin)