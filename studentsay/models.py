from django.db import models

# Create your models here.
class studentSay(models.Model):
    student_name = models.CharField(max_length=50)
    student_image = models.FileField(upload_to='student/', max_length=100,null=False,default=None)
    student_desc = models.TextField(max_length=150)
    