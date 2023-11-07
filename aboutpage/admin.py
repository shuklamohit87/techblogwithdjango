from django.contrib import admin
from aboutpage.models import aboutData
# Register your models here.
class aboutDataAdmin(admin.ModelAdmin):
    list_display=('ques1','ques2','ques3','ques4','ques5')
admin.site.register(aboutData,aboutDataAdmin)