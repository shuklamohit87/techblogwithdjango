from django.contrib import admin
from students.models import StudentJoined
# Register your models here.
class StudentJoinedAdmin(admin.ModelAdmin):
    list_display=('id','name','email','facultyname','phoneno','coursestartdate','courseenddate','createddate','center','course','sign_auth')
admin.site.register(StudentJoined,StudentJoinedAdmin)