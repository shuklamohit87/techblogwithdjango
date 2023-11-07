from django.contrib import admin
from quicklinks.models import quickLinks
# Register your models here.
class quickLinksAdmin(admin.ModelAdmin):
    list_display=('footermenu',)
admin.site.register(quickLinks,quickLinksAdmin)