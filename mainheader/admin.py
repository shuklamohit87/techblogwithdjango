from django.contrib import admin
from mainheader.models import mainHeader
# Register your models here.
class mainHeaderAdmin(admin.ModelAdmin):
    list_display=('header_title','header_social_url_twt','header_socila_url_link','header_social_url_fb','header_social_url_insta','header_social_url_yt','header_contact','header_email')
admin.site.register(mainHeader,mainHeaderAdmin)