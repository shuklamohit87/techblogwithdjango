from django.db import models
from postcategories.models import postCategories
from certificaterequest.models import ChooseCenter
from phone_field import PhoneField
from tinymce.models import HTMLField
# Create your models here.
class EnquiryNow(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact =PhoneField(blank=True, help_text='Contact Number')
    course = models.ForeignKey("postcategories.postCategories",on_delete=models.CASCADE)
    center = models.ForeignKey("certificaterequest.ChooseCenter",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class CampusTraining(models.Model):
    image = models.FileField(upload_to='services/', max_length=250,null=False,default=None)
    description_one =   HTMLField()
    heading_two = models.CharField(max_length=250)
    description_two = HTMLField()
    heading_three = models.CharField(max_length=250)
    description_three = HTMLField()
    heading_four = models.CharField(max_length=250)
    description_four = HTMLField()
    heading_five = models.CharField(max_length=250)
    description_five = HTMLField()
    heading_six = models.CharField(max_length=250)
    description_six = HTMLField()
    
class CorporateTraining(models.Model):
    image = models.FileField(upload_to='services/', max_length=250,null=False,default=None)
    description_one =   HTMLField()
    heading_two = models.CharField(max_length=250)
    description_two = HTMLField()
    heading_three = models.CharField(max_length=250)
    description_three = HTMLField()
    heading_four = models.CharField(max_length=250)
    description_four = HTMLField()    
    
class ClassRoomTraining(models.Model):
    image = models.FileField(upload_to='services/', max_length=250,null=False,default=None)
    description_one =   HTMLField()
    heading_two = models.CharField(max_length=250)
    description_two = HTMLField()
    heading_three = models.CharField(max_length=250)
    description_three = HTMLField()
    heading_four = models.CharField(max_length=250)
    description_four = HTMLField()    
    
class IndustrialTraining(models.Model):
    image = models.FileField(upload_to='services/', max_length=250,null=False,default=None)
    description_one =   HTMLField()
    heading_two = models.CharField(max_length=250)
    description_two = HTMLField()
    heading_three = models.CharField(max_length=250)
    description_three = HTMLField()
    heading_four = models.CharField(max_length=250)
    description_four = HTMLField()
    heading_five = models.CharField(max_length=250)
    description_five = HTMLField()   