# Generated by Django 4.2.5 on 2023-09-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_app', '0003_urldata_url_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='urldata',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]