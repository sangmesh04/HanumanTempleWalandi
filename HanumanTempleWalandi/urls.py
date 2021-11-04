"""HanumanTempleWalandi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from home import views
from adminpanel import views1
from checkout import views2
urlpatterns = [
    path('hanumanadmin/', admin.site.urls),
    path('',include('home.urls')),
    path('trust',views.trust),
    path('donate',views.donate),
    path('feedback',views.feedback),
    path('temple',views.temple),
    path('construction',views.construction),
    path('contact',views.contact),
    path('reciept',views.reciept),
    path('adminlogin',views1.adminlogin),
    path('dashboard',views1.dashboard),
    path('cashdonors',views1.cashdonors),
    path('donors',views1.donors),
    path('event',views1.event),
    path('payment',views2.payment),
    path('payu_checkout',views2.payu_checkout),
    path('success',views2.payu_success),
    path('failure',views2.payu_failure),
    path('signout',views1.signout),
    path('F_R',views1.feedbackReviews),
    path('paycash',views.paycash),
    path('addDonor',views1.addDonor),
    path('addEvent',views1.addEvent),
    path('cashRecieved',views1.cashRecieved),
     path('addExpenditure',views1.addExpenditure),
]
