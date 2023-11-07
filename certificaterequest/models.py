from django.db import models
# from django import forms
# from django.utils.timezone import LocalTim
# from datetime import date
# Create your models here.
class ChooseCenter(models.Model):
    centername=models.CharField(max_length=50)
    
    def __str__(self):
        return self.centername
    
class CertificateRequest(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=254,null=True)
    course=models.CharField(max_length=50,null=True)
    center= models.ForeignKey("ChooseCenter",on_delete=models.CASCADE)
    facultyname=models.CharField(max_length=50,null=True)
    studentid=models.CharField(max_length=50,null=True)
    phoneno = models.CharField(max_length=10,null=True)
    startdate=models.DateField(auto_now=False, auto_now_add=False,null=True)
    enddate=models.DateField(auto_now=False, auto_now_add=False,null=True)
