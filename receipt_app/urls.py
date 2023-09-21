from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings as conf_settings

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/<str:invoice_number>/<str:channel>/<str:account_no>/<str:account_name>/<str:description>/<str:amount>/<str:date>', views.receipt_generator, name='receipt_generator'),
    path('<str:url_id>', views.url_redirect, name='url_redirect'),
    path('receipt/<str:invoice_number>/<str:channel>/<str:account_no>/<str:account_name>/<str:description>/<str:amount>/<str:date>', views.show_receipt, name='show_receipt')
] + static(conf_settings.STATIC_URL, document_root=conf_settings.STATIC_ROOT)

