from django.urls import path
from . import views

urlpatterns = [
    path('cCustomer/',views.create_customer_view,name='cCustomerpg'),
    path('sCustomer/',views.show_customer_view,name='sCustomerpg'),
]