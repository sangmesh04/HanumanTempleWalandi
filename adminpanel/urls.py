from django.contrib import admin
from django.urls import path,include

from adminpanel import views1

urlpatterns = [
    path('hanumanadmin/', admin.site.urls),
    path('dashboard',views1.dashboard),
    path('adminlogin',views1.adminlogin),
    path('cashdonors',views1.cashdonors),
    path('donors',views1.donors),
    path('event',views1.event),
    path('signout',views1.signout),
    path('addDonor',views1.addDonor),
    path('addEvent',views1.addEvent),
    path('addExpenditure',views1.addExpenditure),
]