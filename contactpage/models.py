from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class contactData(models.Model):
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14) 
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    offaddress = models.TextField()
    googlemap1 = models.CharField(max_length=250)
    googlemap2 = models.TextField()
    contactinfo = models.TextField()
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=300)
    message = models.TextField()
        