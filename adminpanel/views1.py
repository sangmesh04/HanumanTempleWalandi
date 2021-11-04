
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from home.models import Donor, Event, Feedback, Contact, Expenditure

# Include the `fusioncharts.py` file that contains functions to embed the charts.
# from fusioncharts import FusionCharts

# Loading Data from a Ordered Dictionary
# Example to create a column 2D chart with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.
# Create your views here.
def adminlogin(request):
    if request.method == 'POST':
        # balance = Donor.objects.all()
        # expediture = Expenditure.objects.all()
        # bala = 0
        # expe = 0
        # for j in expediture[0:]:
        #     expe = expe + int(j.expenditure_amount)
        # for i in balance[0:]:
        #     bala = bala + int(i.donor_amount)
        # bala = bala - expe
        # Making Checkout form into dictionary
        # data = {k: v[0] for k, v in dict(request.POST).items()}
        # user = authenticate(username=data['loginId'], password=data['password'])
        username = request.POST['loginId']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return render(request,'dashboard.html',{'status': 'Successfully donor added!','display':'none'})
    return render(request,'adminlogin.html')
        
    
@login_required(login_url=None)
def dashboard(request):
    balance = Donor.objects.all()
    expediture = Expenditure.objects.all()
    bala = 0
    expe = 0
    for j in expediture[0:]:
        expe = expe + int(j.expenditure_amount)
    for i in balance[0:]:
        bala = bala + float(i.donor_amount)
    bala = bala - expe
    return render(request,'dashboard.html',{'status': 'Successfully donor added!','display':'none','expendi':expediture, 'balance':bala, 'expenditure':expe})



@login_required(login_url='adminlogin')
def cashRecieved(request):
    donor_firstname = request.POST['firstname']
    donor_txnid = request.POST['txnid']
    donors = Donor.objects.all()
    count = 0
    for i in donors[0:]:
        if(i.donor_first_name == donor_firstname and i.donor_txnid == donor_txnid):
            i.payment_status = 'success'
            i.donoration_time = datetime.now()
            i.save()
    donors = Donor.objects.all()
    count = 0
    for i in donors[0:]:
        if(i.payment_status == 'pending'):
            count += 1
    params = {'donor':donors, 'range': range(len(donors)), 'count' : count}
    return render(request,'cashdonors.html',params)


@login_required(login_url='adminlogin')
def cashdonors(request):
    donors = Donor.objects.all()
    count = 0
    for i in donors[0:]:
        if(i.payment_status == 'pending'):
            count += 1
    params = {'donor':donors, 'range': range(len(donors)), 'count' : count}
    return render(request,'cashdonors.html',params)

@login_required(login_url='adminlogin')
def donors(request):
    donors = Donor.objects.all()
    count = 0
    for i in donors[0:]:
        if(i.payment_status == 'success'):
            count += 1
    params = {'donor':donors, 'range': range(len(donors)), 'count' : count}
    return render(request,'donors.html',params)

@login_required(login_url='adminlogin')
def event(request):
    events = Event.objects.order_by('eventEndDate').reverse()
    currentDate = date.today()
    currentDate = currentDate.strftime("%Y-%m-%d")
    params = {'event':events , 'currentdate' :str(currentDate), 'count': len(events)}
    return render(request,'event.html',params)
    # return render(request,'event.html')

@login_required(login_url=None)
def feedbackReviews(request):
    feedbacks = Feedback.objects.order_by('feedback_time').reverse()
    reviews = Contact.objects.order_by('contact_time').reverse()
    params = {'feedback':feedbacks, 'review':reviews, 'Fcount':len(feedbacks), 'Rcount': len(reviews)}
    return render(request,'feedback_reviews.html', params )

def signout(request):
    logout(request)
    return render(request,'adminlogin.html')

@login_required(login_url=None)
def addDonor(request):
    if request.method == 'POST':
        balance = Donor.objects.all()
        expediture = Expenditure.objects.all()
        bala = 0
        expe = 0
        for j in expediture[0:]:
            expe = expe + int(j.expenditure_amount)
        for i in balance[0:]:
            bala = bala + int(i.donor_amount)
        bala = bala - expe
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        organization = request.POST['organizationName']
        adddress = request.POST['address']
        amount = request.POST['amount']
        txnid = request.POST['txnid']
        status = 'success'
        time = datetime.now()
        donorQuery = Donor(donor_first_name=firstname,donor_last_name=lastname,donor_phone_number=phone,donor_organization_name=organization,donor_address=adddress,donor_amount=amount,donor_txnid=txnid,donoration_time=time,payment_status=status)
        donorQuery.save()
        return render(request,'dashboard.html',{'status': 'Donor added successfully!','expendi':expediture,'display':'block', 'balance':bala, 'expenditure':expe})

@login_required(login_url=None)
def addEvent(request):
    if request.method == 'POST':
        balance = Donor.objects.all()
        expediture = Expenditure.objects.all()
        bala = 0
        expe = 0
        for j in expediture[0:]:
            expe = expe + int(j.expenditure_amount)
        for i in balance[0:]:
            bala = bala + int(i.donor_amount)
        bala = bala - expe
        eventname = request.POST['eventname']
        eventstartdate = request.POST['eventstartdate']
        eventenddate = request.POST['eventenddate']
        eventdesc = request.POST['eventdesc']
        eventQuery = Event(eventName=eventname,eventStartDate=eventstartdate,eventEndDate=eventenddate,Descreption=eventdesc)
        eventQuery.save()
        return render(request,'dashboard.html',{'status': 'Event added successfully!','expendi':expediture,'display':'block', 'balance':bala, 'expenditure':expe})

@login_required(login_url=None)
def addExpenditure(request):
    if request.method == 'POST':
        balance = Donor.objects.all()
        expediture = Expenditure.objects.all()
        bala = 0
        expe = 0
        for j in expediture[0:]:
            expe = expe + int(j.expenditure_amount)
        for i in balance[0:]:
            bala = bala + int(i.donor_amount)
        bala = bala - expe
        expendName = request.POST['expendName']
        txnid = request.POST['txnid']
        work = request.POST['work']
        amount = request.POST['amount']
        expenditureQuery = Expenditure(expenditure_txnid=txnid,expenditure_by_name=expendName,expenditure_work=work,expenditure_amount=amount)
        expenditureQuery.save()
        return render(request,'dashboard.html',{'status': 'Expenditure added successfully!','expendi':expediture,'display':'block', 'balance':bala, 'expenditure':expe})