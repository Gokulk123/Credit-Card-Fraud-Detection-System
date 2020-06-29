"""credit_card_fraud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .credit_card_fraud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('banklogin/',views.banklogin),
    path('customerlogin/',views.customerlogin),
    path('analyserlogin/',views.analyserlogin),
    path('bankhome/',views.bankhome),
    path('add_customer_details/',views.add_customer_details),
    path('add_account_details/',views.add_account_details),
    path('customerhome/',views.customerhome),
    path('analyserhome/',views.analyserhome),
    path('bank_sign/',views.bank_sign),
    path('bank_logout/',views.bank_logout),
    path('customer_sign/',views.customer_sign),
    path('customer_logout/',views.customer_logout),
    path('customer_profiles/',views.customer_profiles),
    path('view_customer_details/',views.view_customer_details),
    path('customer_account/',views.customer_account),
    path('view_account_details/',views.view_account_details),
    path('cus_profile/',views.cus_profile),
    path('update_pro/',views.update_pro),
    path('acct_details/',views.acct_details),
    path('add_payment/',views.add_payment),
    path('save_payment/',views.save_payment),
    path('view_balance/',views.view_balance),
    path('make_transaction/',views.make_transaction),
    path('save_transaction/',views.save_transaction),
    path('our_transaction/',views.our_transaction),
    path('all_transaction/',views.all_transaction),
]
