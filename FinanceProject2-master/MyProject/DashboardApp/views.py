from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerModelForm
from MyApp.models import LoanDetails

def dashboardView(request):
    return render(request,"DashboardApp/base.html")

def addcustomerview(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_cus')
    template_name = 'DashboardApp/personaldetail.html'
    context = {'form':form}
    return render(request,template_name,context)

def customerdetailview(request):
    return render(request,"DashboardApp/customerdetail.html")

def LoanDetailsView(request):
    loandetails_obj  = LoanDetails.objects.all()
    template_name = "DashboardApp/showloandetails.html"
    context = {'loandetails_obj': loandetails_obj}
    return render(request, template_name, context)
