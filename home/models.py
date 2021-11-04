from django.db import models

# from home.views import feedback

# Create your models here.
class Feedback(models.Model):
    feedback_first_name = models.CharField(max_length=100)
    feedback_last_name = models.CharField(max_length=100)
    feedback_mobile_number = models.CharField(max_length=12)
    feedback_text = models.TextField()
    feedback_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_first_name + " " + self.feedback_last_name+ " "+ str(self.feedback_time)

class Contact(models.Model):
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_mobile_number = models.CharField(max_length=12)
    contact_text = models.TextField()
    contact_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_first_name + " " + self.contact_last_name + " " +str(self.contact_time)


class Donor(models.Model):
    donor_first_name = models.CharField(max_length=100)
    donor_last_name = models.CharField(max_length=100)
    donor_phone_number = models.CharField(max_length=12)
    donor_organization_name = models.CharField(max_length=100)
    donor_email = models.CharField(max_length=100)
    donor_address =models.CharField(max_length=300)
    donor_country = models.CharField(max_length=100)
    donor_state = models.CharField(max_length=100)
    donor_city = models.CharField(max_length=100)
    donor_zip = models.CharField(max_length=10)
    donor_amount = models.CharField(max_length=100)
    donor_txnid = models.CharField(max_length=20)
    donoration_time = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.donor_first_name + " " +self.donor_last_name + " " + self.payment_status + " " + str(self.donoration_time)


class Event(models.Model):
    eventName = models.CharField(max_length=200)
    eventStartDate = models.CharField(max_length=200)
    eventEndDate = models.CharField(max_length=200)
    Descreption = models.TextField()

    def __str__(self):
        return self.eventName 

class Expenditure(models.Model):
    expenditure_txnid = models.CharField(max_length=50)
    expenditure_by_name = models.CharField(max_length=100)
    expenditure_work = models.CharField(max_length=200)
    expenditure_date = models.DateTimeField(auto_now_add=True)
    expenditure_amount = models.CharField(max_length=50)

    def __str__(self):
        return self.expenditure_by_name + " " + self.expenditure_amount + " " + str(self.expenditure_date)