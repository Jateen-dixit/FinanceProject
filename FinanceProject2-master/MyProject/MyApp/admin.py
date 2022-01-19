from django.contrib import admin
from .models import LoanDetails

# Register your models here.
class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','dob','mobile','email','pan_number','required_loan','cibil_score','is_eligible']

admin.site.register(LoanDetails, LoanDetailsAdmin)