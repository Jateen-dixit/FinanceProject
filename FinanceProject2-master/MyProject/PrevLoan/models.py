from django.db import models
from Customer.models import Customer

CHOICES = (
    ('PERSONAL', 'Personal'),
    ('VEHICLE', 'Vehicle'),
    ('HOME', 'Home')
)


class PrevLoan(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    account_no = models.IntegerField()
    ifsc_code = models.CharField(max_length=11)
    micr_code = models.CharField(max_length=9)
    loan_amount = models.FloatField()
    loan_type = models.CharField(max_length=10, choices=CHOICES)
    loan_tenure = models.FloatField()
    amount_paid = models.FloatField()
    amount_remaining = models.FloatField()
