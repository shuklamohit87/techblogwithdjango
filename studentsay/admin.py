from django.contrib import admin
from studentsay.models import studentSay
# Register your models here.
class StudentSayAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_image','student_desc')
admin.site.register(studentSay,StudentSayAdmin)