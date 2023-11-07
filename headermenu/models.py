from django.db import models

# Create your models here.
class headerMenu(models.Model):
    menu=models.CharField(max_length=50)
    