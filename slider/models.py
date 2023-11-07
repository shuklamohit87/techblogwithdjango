from django.db import models

# Create your models here.
class sliders(models.Model):
    slider_image = models.FileField(upload_to='slider/', max_length=100,default=None,null=False)
    slider_tag = models.CharField(max_length=100)
    slider_title = models.TextField(max_length=150)
    slider_button = models.CharField(max_length=50)