from django.shortcuts import render, redirect
from .models import SanctionedLoan
from .forms import SanctionedLoanModelForm


def home_view(request):
    return render(request, template_name='index.html')


def create_sanctionedoan_view(request):
    form = SanctionedLoanModelForm()
    if request.method == 'POST':
        form = SanctionedLoanModelForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('homepage')
    return render(request, template_name='DashboardApp/sanctioned_loan.html', context={'form': form})
