from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class termPolicy(models.Model):
    termcontent = HTMLField()