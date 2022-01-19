from django.shortcuts import render, redirect
from .forms import GuarantorModelForm
from .models import Guarantor
from django.views import View



class add_guarantor_view(View):
    def get(self, request):
        form = GuarantorModelForm()
        template_name = 'DashboardApp/guarantordetails.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        form = GuarantorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminhomepg")
        template_name = 'DashboardApp/guarantordetails.html'
        context = {'form': form}
        return render(request, template_name, context)


class show_guarantor_view(View):
    def get(self, request):
        guarantor = Guarantor.objects.all()
        print(guarantor)
        template_name = 'customer_guarantor_app/showguarantor.html'
        context = {'guarantor': guarantor}
        return render(request, template_name, context)


class update_guarantor_view(View):
    def get(self, request, i):
        guarantor = Guarantor.objects.get(id=i)
        form = GuarantorModelForm(instance=guarantor)
        template_name = 'customer_guarantor_app/guarantordetails.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, i):
        guarantor = Guarantor.objects.get(id=i)
        form = GuarantorModelForm(request.POST, instance=guarantor)
        if form.is_valid():
            form.save()
            return redirect("showguarantor")
        template_name = 'customer_guarantor_app/guarantordetails.html'
        context = {'form': form}
        return render(request, template_name, context)


class delete_guarantor_view(View):
    def get(self, request, i):
        guarantor = Guarantor.objects.get(id=i)
        template_name = 'customer_guarantor_app/deleteguarantor.html'
        context = {'guarantor': guarantor}
        return render(request, template_name, context)

    def post(self, request, i):
        guarantor = Guarantor.objects.get(id=i)
        guarantor.delete()
        return redirect("showguarantor")
