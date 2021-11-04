from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# from django.contrib.auth.decorators import login_required
# Import Payu from Paywix
from paywix.payu import Payu
import random
from home.models import Donor

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

# Create Payu Object for making transaction
# The given arguments are mandatory
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)

# Create your views here.
def payment(request):
    return render(request,'payu.html')


@csrf_exempt
def payu_checkout(request):
    request.method = 'POST'
    if request.method == 'POST':
        # Making Checkout form into dictionary
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        # The dictionary data  should be contains following details
        data = { 'amount': data['amount'], 
            'firstname': data['firstname'], 
            'email': data['email'],
            'phone': data['phone'], 'productinfo': 'Donation to HMWT', 
            'lastname': data['lastname'], 'address1': data['address'], 
            'address2': data['organizationName'], 'city': data['city'], 
            'state': data['state'], 'country': data['country'], 
            'zipcode': data['zipcode'], 'udf1':  '', 
            'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
        }

        # No Transactio ID's, Create new with paywix, it's not mandatory
        # Create your own
        # Create transaction Id with payu and verify with table it's not existed
        txnid = "HMWT" + str(random.randrange(100000,999999))
        data.update({"txnid": txnid})
        payu_data = payu.transaction(**data)
        return render(request, 'payu_checkout.html', {"posted": payu_data})
    return HttpResponse("Error!")


# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    donorData = response['return_data']
    donorEntry = Donor(donor_first_name=donorData['firstname'],donor_last_name=donorData['lastname'],donor_phone_number=donorData['phone'],donor_organization_name=donorData['address2'],donor_email=donorData['email'],donor_address=donorData['address1'],donor_country=donorData['country'],donor_state=donorData['state'],donor_city=donorData['city'],donor_zip=donorData['zipcode'],donor_amount=donorData['amount'],donor_txnid=donorData['txnid'],donoration_time=donorData['addedon'],payment_status=donorData['status'])
    donorEntry.save()
    return render(request,'donate.html',{'status': 'Thank you for donating! We recieved ','state':'success','display':'block','amount':donorData['amount']})
    # return JsonResponse(response)

# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    donorData = response['return_data']
    return render(request,'donate.html',{'state':'danger','status': 'Failure in payment to send ','display':'block','amount':donorData['amount']})
    # return JsonResponse(response)
