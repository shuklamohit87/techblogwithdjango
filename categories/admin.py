from django.contrib import admin

# Register your models here.
from categories.models import Course
class categoriesAdmin(admin.ModelAdmin):
    list_display=('id','course_image','course_title')
admin.site.register(Course,categoriesAdmin)
