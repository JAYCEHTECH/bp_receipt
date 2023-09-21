from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/<str:invoice_number>/<str:channel>/<str:account_no>/<str:account_name>/<str:description>/<str:amount>', views.receipt_generator, name='receipt_generator'),
    path('<str:url_id>', views.url_redirect, name='url_redirect'),
    path('receipt/<str:invoice_number>/<str:channel>/<str:account_no>/<str:account_name>/<str:description>/<str:amount>', views.show_receipt, name='show_receipt')
]

