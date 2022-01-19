from django.shortcuts import render, redirect
from .forms import PrevLoanForm
from .models import PrevLoan


def create_prevloan_view(request):
    form = PrevLoanForm()
    if request.method == 'POST':
        form = PrevLoanForm(request.POST)
        print("method is post")
        print(request.POST)

        if form.is_valid():
            print("FOrm is valid")
            form.save()
            return redirect('addguarantor')
        print("Form is not valid")
    template_name = 'DashboardApp/prevloandetails.html'
    context = {'form': form}
    return render(request, template_name, context)


def show_prevloan_view(request):
    bank = PrevLoan.objects.all()
    template_name = 'show.html'
    context = {'bank': bank}
    return render(request, template_name, context)


def delete_prevloan_view(request, i):
    bank = PrevLoan.objects.get(id=i)
    bank.delete()
    return redirect('rPrevLoanpg')


def update_prevloan_view(request, i):
    bank = PrevLoan.objects.get(id=i)
    form = PrevLoanForm(instance=bank)
    if request.method == 'POST':
        form = PrevLoanForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('rPrevLoanpg')
    context = {'form': form}
    template_name = 'add.html'
    return render(request, template_name, context)
