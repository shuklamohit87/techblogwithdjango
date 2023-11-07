from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Course(models.Model):
    course_image=models.FileField(upload_to="course/", max_length=250,null=False,default=None)
    course_title=models.CharField(max_length=50)
    course_detail = HTMLField(null=True)
    course_brouchre = models.FileField(upload_to="course-brouchre/", max_length=250,null=True,default=None)
def __str__(self):
    return self.id