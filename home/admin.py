from django.contrib import admin

from home.views import donate
from .models import Feedback,Contact,Donor,Event,Expenditure
# Register your models here.
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Donor)
admin.site.register(Event)
admin.site.register(Expenditure)