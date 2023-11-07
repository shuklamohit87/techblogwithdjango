from django.contrib import admin
from policy.models import Policy
# Register your models here.
class PolicyAdmin(admin.ModelAdmin):
    list_display=['policycontent']
admin.site.register(Policy,PolicyAdmin)