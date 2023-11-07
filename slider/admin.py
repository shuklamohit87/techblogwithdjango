from django.contrib import admin
from slider.models import sliders
# Register your models here.
class sliderAdmin(admin.ModelAdmin):
    list_display=('slider_image','slider_title','slider_tag','slider_button')
admin.site.register(sliders,sliderAdmin)
