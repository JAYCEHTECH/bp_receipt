from django.db import models


# Create your models here.
class UrlData(models.Model):
    url = models.CharField(max_length=200, null=True, blank=False)
    short_url = models.CharField(max_length=100, null=True, blank=True)
    url_id = models.CharField(max_length=10, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
