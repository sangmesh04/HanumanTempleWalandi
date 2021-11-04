from django.urls import path
from checkout import views2
urlpatterns = [
    path('payu_checkout',views2.payu_checkout,name="Payment"),
    path('success',views2.payu_success),
    path('failure',views2.payu_failure),
]
