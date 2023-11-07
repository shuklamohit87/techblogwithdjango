from django.contrib import admin
from headermenu.models import headerMenu
# Register your models here.
class headerMenuAdmin(admin.ModelAdmin):
    list_display=['menu']
admin.site.register(headerMenu,headerMenuAdmin)