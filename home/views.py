from typing import ContextManager
from django.shortcuts import render, HttpResponse

from adminpanel.views1 import event
from .models import Feedback, Contact, Donor, Event
from datetime import datetime, date
# Create your views here.
def home(request):
    events = Event.objects.order_by('eventEndDate').reverse()
    currentDate = date.today()
    currentDate = currentDate.strftime("%Y-%m-%d")
    params = {'event':events , 'currentdate' :str(currentDate)}
    return render(request,'home.html',params)
    # return HttpResponse('Thsi is home page')

def trust(request):
    return render(request,'trust.html')

def donate(request):
    return render(request,'donate.html',{'display':'none'})

def feedback(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        feedbackphone = request.POST['feedphone']
        feedbackText = request.POST['feedback']
        feedbackEntry = Feedback(feedback_first_name=firstname,feedback_last_name=lastname,feedback_mobile_number=feedbackphone,feedback_text=feedbackText)
        feedbackEntry.save()
        return render(request,'feedback.html',{'status': 'Your feedback has been submitted!','display':'block'})
    return render(request,'feedback.html',{'display':'none'})

def temple(request):
    return render(request,'temple.html')

def construction(request):
    return render(request,'construction.html')

def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contactphone = request.POST['contactphone']
        contactText = request.POST['contact']
        contactEntry = Contact(contact_first_name=firstname,contact_last_name=lastname,contact_mobile_number=contactphone,contact_text=contactText)
        contactEntry.save()
        return render(request,'contact.html',{'status': 'Your query has been submitted!','display':'block'})
    return render(request,'contact.html',{'display':'none'})

def reciept(request):
    return render(request,'reciept.html')

def payment(request):
    return render(request,'payment.php')


def paycash(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        organization = request.POST['organizationName']
        adddress = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        amount = request.POST['amount']
        txnid = request.POST['txnid']
        status = 'pending'
        time = datetime.now()
        donorQuery = Donor(donor_first_name=firstname,donor_last_name=lastname,donor_phone_number=phone,donor_organization_name=organization,donor_email=email,donor_address=adddress,donor_country=country,donor_state=state,donor_city=city,donor_zip=zipcode,donor_amount=amount,donor_txnid=txnid,donoration_time=time,payment_status=status)
        donorQuery.save()
        return render(request,'donate.html',{'status': 'Thank you for donating! We will collect money value ','state':'success','display':'block','amount':amount})


  