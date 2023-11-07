from django.contrib import admin
# from headerservices.models import EnquiryNow,CampusTraining,CorporateTraining,ClassRoomTraining,IndustrialTraining
from .models import *

# Register your models here.
class EnquiryNowAdmin(admin.ModelAdmin):
    list_display=('name','email','contact','course','center')

admin.site.register(EnquiryNow,EnquiryNowAdmin)

class CampusTrainingAdmin(admin.ModelAdmin):
    list_display=('image','description_one','heading_two','description_two','heading_three','description_three','heading_four','description_four','heading_five','description_five','heading_six','description_six')

class CorporateTrainingAdmin(admin.ModelAdmin):
    list_display=('image','description_one','heading_two','description_two','heading_three','description_three','heading_four','description_four','heading_five','description_five','heading_six','description_six')

class ClassRoomTrainingAdmin(admin.ModelAdmin):
    list_display=('image','description_one','heading_two','description_two','heading_three','description_three','heading_four','description_four','heading_five','description_five','heading_six','description_six')

class IndustrialTrainingAdmin(admin.ModelAdmin):
    list_display=('image','description_one','heading_two','description_two','heading_three','description_three','heading_four','description_four','heading_five','description_five','heading_six','description_six')

admin.site.register(CampusTraining)
admin.site.register(CorporateTraining)
admin.site.register(ClassRoomTraining)
admin.site.register(IndustrialTraining)