from django.contrib import admin
from django.urls import path,include
from home import views
from adminpanel import views1
from checkout import views2
urlpatterns = [
    path('hanumanadmin/', admin.site.urls),
    path('',views.home),
    path('trust',views.trust,name='Trust'),
    path('donate',views.donate,name='Donate Now'),
    path('feedback',views.feedback,name='Feedback'),
    path('temple',views.temple,name='Main Temple'),
    path('construction',views.construction,name='Construction and Design'),
    path('contact',views.contact,name='Contact Us'),
    path('reciept',views.reciept,name="Get Donation Reciept"),
    path('adminlogin',views1.adminlogin,name="Admin Login"),
    path('dashboard',views1.dashboard,name="Dashboard"),
    path('cashdonors',views1.cashdonors),
    path('donors',views1.donors),
    path('event',views1.event),
    path('payment',views2.payment),
    path('success',views2.payu_success),
    path('failure',views2.payu_failure),
    path('paycash',views.paycash),
    path('cashRecieved',views1.cashRecieved),
     path('addExpenditure',views1.addExpenditure),
]
