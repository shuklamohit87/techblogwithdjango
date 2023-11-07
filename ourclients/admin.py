from django.contrib import admin
from ourclients.models import ourClients
# Register your models here.
class ourClientAdmin(admin.ModelAdmin):
    list_display=('client_name','client_image')
admin.site.register(ourClients,ourClientAdmin)