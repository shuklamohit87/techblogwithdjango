from django.contrib import admin
from certificaterequest.models import CertificateRequest
from certificaterequest.models import ChooseCenter
# Register your models here.
class ChooseCenterAdmin(admin.ModelAdmin):
    list_display=['centername']
admin.site.register(ChooseCenter,ChooseCenterAdmin)
    
class CertificateRequestAdmin(admin.ModelAdmin):
    list_display=('name','email','course','center','facultyname','studentid','phoneno','startdate','enddate')
admin.site.register(CertificateRequest,CertificateRequestAdmin)