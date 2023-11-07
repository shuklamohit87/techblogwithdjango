from django.contrib import admin
from popularcourse.models import popularCourse
# Register your models here.
class popularCourseAdmin(admin.ModelAdmin):
    list_display=('course_imageone','course_title','course_flag','course_imagetwo')
admin.site.register(popularCourse,popularCourseAdmin) 
   

    