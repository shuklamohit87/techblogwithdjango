from django.db import models

# Create your models here.
class ourClients(models.Model):
    client_name = models.CharField(max_length=50)
    client_image = models.FileField(upload_to='clients/',  max_length=100,null=False,default=None)