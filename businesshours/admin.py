from django.contrib import admin
from businesshours.models import BusinessHours
# Register your models here.
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display=('opendays','specificdayopen','closeday')
admin.site.register(BusinessHours,BusinessHoursAdmin)