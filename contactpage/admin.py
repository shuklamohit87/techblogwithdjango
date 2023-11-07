from django.contrib import admin
from contactpage.models import contactData
from contactpage.models import ContactForm
# Register your models here.
class contactDataAdmin(admin.ModelAdmin):
    list_display=('phone1','phone2','email1','email2','offaddress','googlemap1','googlemap2','contactinfo')
admin.site.register(contactData,contactDataAdmin)

class contactFormAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','phone','message')
admin.site.register(ContactForm,contactFormAdmin)