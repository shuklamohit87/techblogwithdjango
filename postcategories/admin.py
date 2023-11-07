from django.contrib import admin
from postcategories.models import postCategories
# Register your models here.
class postCategoriesAdmin(admin.ModelAdmin):
    list_display = ['category_title']
admin.site.register(postCategories,postCategoriesAdmin)