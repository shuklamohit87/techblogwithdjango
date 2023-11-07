from django.contrib import admin
from placement.models import placeStudent
# Register your models here.
class placeStudentAdmin(admin.ModelAdmin):
    list_display=('studentimg','studentname','studentprofile','studentpacakage','studentcompany')
admin.site.register(placeStudent,placeStudentAdmin)