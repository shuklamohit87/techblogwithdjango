from django.db import models

# Create your models here.
class mainHeader(models.Model):
    header_title = models.CharField(max_length=50)
    header_social_url_twt = models.URLField(max_length=200)
    header_socila_url_link = models.URLField(max_length=200)
    header_social_url_fb = models.URLField(max_length=200)
    header_social_url_insta = models.URLField(max_length=200)
    header_social_url_yt = models.URLField(max_length=200)
    header_contact = models.CharField(max_length=12)
    header_email = models.EmailField(max_length=254)
    