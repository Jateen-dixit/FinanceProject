from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homeView, name="homepage"),
    path('nav/el/',eligibility_view,name='eligibility'),
    path('nav/fet/',feature_view,name='features'),
    path('nav/fee/',fees_charges_view,name='fee_charges'),
    path('nav/doc/',req_doc_view,name='req_doc'),
    path('login', login_view, name="loginpage"),
    path('nav/emi/',emi_view,name="emipage"),
    path('about/',about_view, name='aboutpage'),
    path('enquiry/',EnquiryView, name="enquirypage"),
    path('addloan/',loandetailsView,name='addloan'),
    path('show1/',show_loandetailsView,name='show'),
    path('update/<int:i>/',update_loandetails,name='update'),
    path('delete/<int:i>/',delete_loandetails,name='delete'),
    path('add/',EnquiryView,name="add_enquiry"),
    path('show/',ShowEnquiryView,name='show_enquiry'),
    path('add/',addview),
    path('show/',show,name='show'),
   

]