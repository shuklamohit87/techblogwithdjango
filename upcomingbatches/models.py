from django.db import models

# Create your models here.
class upcomingBatches(models.Model):
    course_title = models.CharField(max_length=50)
    course_branch = models.CharField(max_length=50)
    course_date = models.DateField()
    course_time = models.TimeField()