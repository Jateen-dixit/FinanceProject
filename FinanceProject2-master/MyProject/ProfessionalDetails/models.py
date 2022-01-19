from django.db import models
from Customer.models import Customer


# Create your models here.



class ProfessionalDetails(models.Model):
    CHOICES = (

        ('ol', 'Online'),
        ('ch', 'Cheque'),
        ('c', 'Cash')
    )


    CHOICES1 = (

        ('sal', 'Salaried'),
        ('self', 'Self-Salaried'),
    )

    CHOICES2 = (

        ('y', 'Yes'),
        ('n', 'No'),
    )

    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    type_employment = models.CharField(max_length=50, choices=CHOICES1)
    designation = models.CharField(max_length=32)
    year_of_exp = models.FloatField()
    joining_date = models.DateField()
    monthly_income = models.FloatField()
    mode_of_salary = models.CharField(max_length=50, choices=CHOICES)
    company_address = models.CharField(max_length=100)

    business_name = models.CharField(max_length=100)
    itr = models.CharField(max_length=50, choices=CHOICES2)
    avg_monthly_income = models.FloatField()
    annual_turnover = models.FloatField()


    def __str__(self):
        return f"{self.company_address},{self.designation},{self.year_of_exp},{self.joining_date},{self.monthly_income},{self.mode_of_salary},{self.business_name},{self.itr},{self.avg_monthly_income},{self.annual_turnover}"



