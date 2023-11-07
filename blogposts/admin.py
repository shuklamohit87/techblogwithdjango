from django.contrib import admin
from blogposts.models import blogPosts
# Register your models here.
class blogPostAdmin(admin.ModelAdmin):
    list_display=('post_slug','post_category','post_tittle','post_image','posted_on','posted_by','post_content')
admin.site.register(blogPosts,blogPostAdmin)

