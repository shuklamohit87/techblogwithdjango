from django.contrib import admin
from footercontact.models import footerContact
from footercontact.models import subscribeNews
# Register your models here.
class footerContactAdmin(admin.ModelAdmin):
    list_display=('address','contact','email')
admin.site.register(footerContact,footerContactAdmin)

class subscribeNewsAdmin(admin.ModelAdmin):
    list_display=['email']
admin.site.register(subscribeNews,subscribeNewsAdmin)