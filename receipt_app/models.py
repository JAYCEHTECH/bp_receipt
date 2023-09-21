from django.contrib.auth.models import AbstractUser
from django.db import models


# # Create your models here.
# # Create your models here.
# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=100, null=False, blank=False)
#     last_name = models.CharField(max_length=100, null=False, blank=False)
#     username = models.CharField(max_length=100, null=False, blank=False, unique=True)
#     email = models.EmailField(max_length=250, null=False, blank=False)
#     wallet = models.FloatField(null=True, blank=True, default=0.0)
#     phone = models.PositiveIntegerField(null=True, blank=True)
#     password1 = models.CharField(max_length=100, null=False, blank=False)
#     password2 = models.CharField(max_length=100, null=False, blank=False)
#

class UrlData(models.Model):
    url = models.CharField(max_length=200, null=True, blank=False)
    short_url = models.CharField(max_length=100, null=True, blank=True)
    url_id = models.CharField(max_length=10, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
