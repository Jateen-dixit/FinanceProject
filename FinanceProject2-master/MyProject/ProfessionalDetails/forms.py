from django import forms
from .models import *


class SalariedModelForm(forms.ModelForm):
    class Meta:
        model = ProfessionalDetails
        fields = ['type_employment', 'designation', 'year_of_exp', 'joining_date', 'monthly_income', 'mode_of_salary', 'company_address']
        labels = {
            'year_of_exp': 'Year of Experience',
            'type_employment': 'Type of Employment',
            'joining_date': 'Joining Date',
            'monthly_income': 'Monthly Income',
            'company_address': 'Company Address',
            'mode_of_salary': 'Select Mode of Salary Payment'

        }

        widgets = {

            'designation': forms.TextInput(attrs={'placeholder': 'Enter Your Designation'}),
            'joining_date': forms.TextInput(attrs={'placeholder': 'Enter Date of Joining'}),
            'year_of_exp': forms.TextInput(attrs={'placeholder':'Experience in Years'}),
            'monthly_income': forms.TextInput(attrs={'placeholder':'Enter Income in Thousands'}),
            'company_address': forms.TextInput(attrs={'placeholder': 'Enter Company Address'}),
        }


class SelfSalariedModelForm(forms.ModelForm):
    class Meta:
        model = ProfessionalDetails
        fields = ['business_name', 'itr', 'avg_monthly_income', 'annual_turnover']
        labels ={
            'itr': 'Have you filed IT returs for the last 2 years? ',
            'business_name': 'Business Name',
            'avg_monthly_income':'Average Monthly Income',
            'annual_turnover':'Annual Turnover'

        }

        widgets = {
            'business_name': forms.TextInput(attrs={'placeholder': 'Enter Business Name'}),
            'avg_monthly_income': forms.TextInput(attrs={'placeholder': 'Enter Income in Thousands'}),
            'annual_turnover': forms.TextInput(attrs={'placeholder':'Enter Turnover in Lakhs'}),
        }