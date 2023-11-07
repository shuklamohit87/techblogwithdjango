from django.db import models

# Create your models here.
class footerContact(models.Model):
    address=models.CharField( max_length=50)
    contact=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)

class subscribeNews(models.Model):
    email=models.EmailField(max_length=254)