from django.db import models

# Create your models here.
class postCategories(models.Model):
    category_title = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.category_title