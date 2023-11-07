from django.db import models

# Create your models here.
class BusinessHours(models.Model):
    opendays = models.CharField(max_length=50)
    specificdayopen = models.CharField(max_length=50)
    closeday = models.CharField(max_length=50)