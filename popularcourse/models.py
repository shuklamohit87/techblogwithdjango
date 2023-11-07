from django.db import models

# Create your models here.
class popularCourse(models.Model):
    course_imageone = models.FileField(upload_to="popularcourse/",max_length=250,null=False,default=None)
    course_title = models.CharField(max_length=50)
    course_flag = models.CharField(max_length=50)
    course_imagetwo =  models.FileField(upload_to="popularcourse/",max_length=250,null=False,default=None)    