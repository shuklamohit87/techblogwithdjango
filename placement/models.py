from django.db import models

# Create your models here.
class placeStudent(models.Model):
    studentimg = models.FileField(upload_to="placestudents/",max_length=250,null=False,default=None)
    studentname = models.CharField(max_length=50)
    studentprofile = models.CharField(max_length=50)
    studentpacakage = models.CharField(max_length=50)
    studentcompany = models.CharField(max_length=50)