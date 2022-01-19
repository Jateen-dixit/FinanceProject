from django.db import models
from Customer.models import Customer


class SanctionedLoan(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    required_loan = models.IntegerField(default=None)
    approved_loan = models.IntegerField()
    tenure = models.IntegerField()
    interest = models.FloatField()
    emi = models.FloatField(default=None)
    is_approved = models.BooleanField(default=False)
