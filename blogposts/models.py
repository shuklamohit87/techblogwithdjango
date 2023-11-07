# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from postcategories.models import postCategories
# Create your models here.
class blogPosts(models.Model):
    post_slug = AutoSlugField(populate_from='post_tittle',unique=True,null=True,default=None)
    post_category = models.ForeignKey(postCategories,on_delete=models.CASCADE,default=1)
    post_tittle = models.CharField(max_length=300)
    post_image = models.FileField(upload_to='postimages/', max_length=250,null=False,default=None)
    posted_on = models.DateField(auto_now=False, auto_now_add=False)
    posted_by = models.CharField(max_length=100)
    post_content = HTMLField()
    
    def __str__(self):
        return self.id