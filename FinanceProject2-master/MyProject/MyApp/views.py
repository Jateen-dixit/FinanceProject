from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import LoanDetails, Enquiry
from .forms import LoanDetailsForm, EnquiryModelForm
import random


def homeView(request):
    return render(request, "index.html")


def eligibility_view(request):
    return render(request, "eligibility.html")


def nav_view(req):
    return render(req, 'navbar_loan.html')


def feature_view(req):
    return render(req, 'features.html')


def fees_charges_view(req):
    return render(req, 'fees_charges.html')


def req_doc_view(req):
    return render(req, 'RequiredDocs.html')


def login_view(req):
    return render(req, 'login.html')


def emi_view(req):
    return render(req, 'emi.html')


def about_view(req):
    return render(req, 'about.html')


def enquiry_view(req):
    return render(req, 'EnquiryForm1.html')


def loandetailsView(request):
    form = LoanDetailsForm()
    if request.method == 'POST':
        form = LoanDetailsForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.cibil_score = random.randint(700, 900)
            user.save()
            return redirect('show')
    template_name = "DashboardApp/loandetails.html"
    context = {'form': form}
    return render(request, template_name, context)


def show_loandetailsView(request):
    customer_list = LoanDetails.objects.all()
    template_name = "DashboardApp/showloandetails.html"
    context = {'customer_list': customer_list}
    return render(request, template_name, context)



def EnquiryView(request):
    form = EnquiryModelForm()
    if request.method == 'POST':
        form = EnquiryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_enquiry')
    template_name = 'EnquiryForm1.html'
    context = {'form': form}
    return render(request, template_name, context)


def ShowEnquiryView(request):
    enquiry_obj = Enquiry.objects.all()
    template_name = 'showenquiry.html'
    context = {'enquiry_obj': enquiry_obj}
    return render(request, template_name, context)


def update_loandetails(request, i):
    customer = LoanDetails.objects.get(id=i)
    form = LoanDetailsForm(instance=customer)
    if request.method == 'POST':
        form = LoanDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = "application.html"
    context = {'form': form}
    return render(request, template_name, context)


def delete_loandetails(request, i):
    customer = LoanDetails.objects.get(id=i)
    customer.delete()
    return redirect("show")


def addview(request):
    form = PrevLoanForm()
    if request.method == 'POST':
        form = PrevLoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)


def show(request):
    bank = PrevLoan.objects.all()
    template_name = 'show.html'
    context = {'bank': bank}
    return render(request, template_name, context)

