from django.shortcuts import render, redirect
from .models import ProfessionalDetails
from .forms import SalariedModelForm, SelfSalariedModelForm


# Create your views here.


def AddSalariedView(request):
    form = SalariedModelForm()
    if request.method == 'POST':
        form = SalariedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cBankDetailspg')
        else:
            print('Form is INVALID')

    context = {'form': form}
    templates_name = 'DashboardApp/add_sal.html'
    return render(request, templates_name, context)


def ShowSalariedView(request):
    show_obj = ProfessionalDetails.objects.all()
    context = {'show_obj': show_obj}
    templates_name = 'show_sal.html'
    return render(request, templates_name, context)


def UpdateSalariedView(request, i):
    update_obj = ProfessionalDetails.objects.get(id=i)
    form = SalariedModelForm(instance=update_obj)
    if request.method == 'POST':
        form = SalariedModelForm(request.POST, instance=update_obj)
        if form.is_valid():
            form.save()
            return redirect('show_sal')

    context = {'form': form}
    templates_name = 'add_sal.html'
    return render(request, templates_name, context)


def DeleteSalariedView(request, i):
    lap = ProfessionalDetails.objects.get(id=i)
    lap.delete()
    return redirect('show_sal')


# Self-Salried Views

def AddSelfSalariedView(request):
    form = SelfSalariedModelForm()
    if request.method == 'POST':
        form = SelfSalariedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_self')
        else:
            print('Form is INVALID')

    context = {'form': form}
    templates_name = 'DashboardApp/add_self.html'
    return render(request, templates_name, context)


def ShowSelfSalariedView(request):
    show_obj = ProfessionalDetails.objects.all()
    context = {'show_obj': show_obj}
    templates_name = 'show_self.html'
    return render(request, templates_name, context)


def UpdateSelfSalariedView(request, i):
    update_obj = ProfessionalDetails.objects.get(id=i)
    form = SelfSalariedModelForm(instance=update_obj)
    if request.method == 'POST':
        form = SelfSalariedModelForm(request.POST, instance=update_obj)
        if form.is_valid():
            form.save()
            return redirect('show_self')

    context = {'form': form}
    templates_name = 'add_self.html'
    return render(request, templates_name, context)


def DeleteSelfSalariedView(request, i):
    lap = ProfessionalDetails.objects.get(id=i)
    lap.delete()
    return redirect('show_self')
