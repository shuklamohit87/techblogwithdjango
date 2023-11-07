from django.contrib import admin
from termpolicy.models import termPolicy
# Register your models here.
class termPolicyAdmin(admin.ModelAdmin):
    list_display=['termcontent']
admin.site.register(termPolicy,termPolicyAdmin)