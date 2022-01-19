from django.urls import path
from . import views

urlpatterns = [
    path('cPrevLoan/',views.create_prevloan_view,name='cPrevLoanpg'),
    path('rPrevLoan/',views.show_prevloan_view,name='rPrevLoanpg'),
    path('dPrevLoan/<int:i>/',views.delete_prevloan_view,name='dPrevLoanpg'),
    path('uPrevLoan/<int:i>/',views.update_prevloan_view,name='uPrevLoanpg'),
]