from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm

def create_customer_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cAddresspg')
    template_name = 'DashboardApp/personaldetail.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_customer_view(request):
    customer = Customer.objects.all()
    template_name = 'Customer/personaldetail.html'
    context = {'customer':customer}
    return render(request,template_name,context)

