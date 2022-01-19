from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard/',views.dashboardView, name="adminhomepg"),
    path('cust/', include('Customer.urls')),
    path('address/', include('AddressApp.urls')),
    path('prevloan/', include('PrevLoan.urls')),
    path('loandetail/', include('LoanApplication.urls')),
    path('bankdetail/', include('BankDetails.urls')),
    path('guarantor/', include('customer_guarantor_app.urls')),
    path('professional/', include('ProfessionalDetails.urls')),
    path('deloan/', views.LoanDetailsView, name="showloandetails")
]