from django.contrib import admin

from receipt_app import models


class UrlDataAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'url_id', 'short_url']


# Register your models here.
admin.site.register(models.UrlData, UrlDataAdmin)







