from django.contrib import admin
from upcomingbatches.models import upcomingBatches
# Register your models here.
class BatchAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_branch','course_date','course_time')
admin.site.register(upcomingBatches,BatchAdmin)