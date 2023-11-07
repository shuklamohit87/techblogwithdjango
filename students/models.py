from django.db import models
from django.utils import timezone
from postcategories.models import postCategories
from certificaterequest.models import ChooseCenter
# Create your models here.
class StudentJoined(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    facultyname = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    coursestartdate = models.DateField(auto_now=False, auto_now_add=False)
    courseenddate = models.DateField(auto_now=False, auto_now_add=False)
    createddate = timezone.now()
    center = models.ForeignKey("certificaterequest.ChooseCenter",on_delete=models.CASCADE)
    course = models.ForeignKey("postcategories.postCategories",on_delete=models.CASCADE)
    sign_auth = models.FileField(upload_to='signingauth/', max_length=250, blank=True)
    
    # def __str__(self):
    #     return self.center
    
    # def __str__(self):
    #     return self.course    