import secrets
from datetime import datetime
from django.http import HttpResponse

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from receipt_app import models


# Create your views here.
def home(request):
    return render(request, "layouts/invoice-1.html")


def receipt_generator(request, invoice_number, channel, account_no, account_name, description, amount):
    if not invoice_number or not channel or not account_no or not account_name or not description or not amount:
        return Response(data={'code': '0002', 'message': 'All parameters were not given'},
                        status=status.HTTP_400_BAD_REQUEST)
    long_url = f'https://receipt-app-2a2vn.ondigitalocean.app/receipt/{invoice_number}/{channel}/{account_no}/{account_name}/{description}/{amount}'
    appender = secrets.token_hex(3)
    short_url = f'https://receipt-app-2a2vn.ondigitalocean.app/{appender}'
    if models.UrlData.objects.filter(invoice_number=invoice_number).exists():
        short_url = models.UrlData.objects.get(invoice_number=invoice_number).short_url
        return Response(data={'code': '0001', 'short_url': short_url, 'message': "Invoice number already exist"}, status=status.HTTP_409_CONFLICT)
    new_url = models.UrlData.objects.create(url=long_url, short_url=short_url, url_id=appender, invoice_number=invoice_number)
    new_url.save()
    return Response(data={'code': '0000', 'short_url': short_url, 'message': 'URL Generation Successful'}, status=status.HTTP_200_OK)


def url_redirect(request, url_id):
    data = models.UrlData.objects.get(url_id=url_id)
    return redirect(data.url)


def show_receipt(request, invoice_number, channel, account_no, account_name, description, amount):
    try:
        short_url = models.UrlData.objects.filter(invoice_number=invoice_number)
        if short_url.exists():
            context = {
                'invoice_no': invoice_number,
                'channel': channel,
                'account_no': account_no,
                'name': account_name,
                'desc': description,
                'amount': amount,
                'date': datetime.now().strftime('%Y-%m-%d')
            }
            return render(request, "layouts/invoice-1.html", context=context)
        else:
            return HttpResponse("Invalid Receipt")
    except models.UrlData.DoesNotExist:
        return HttpResponse("Invalid Receipt")



