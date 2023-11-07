from django.contrib import admin
from privacy.models import privacyPolicy
# Register your models here.
class privacyAdmin(admin.ModelAdmin):
    list_display=['privacycontent']
admin.site.register(privacyPolicy,privacyAdmin)
