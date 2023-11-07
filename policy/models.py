from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Policy(models.Model):
    policycontent = HTMLField()
