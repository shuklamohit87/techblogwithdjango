from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class privacyPolicy(models.Model):
    privacycontent = HTMLField()