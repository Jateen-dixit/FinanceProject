from django.urls import path
from .views import home_view, create_sanctionedoan_view

urlpatterns = [
    path('', home_view, name='homepage'),
    path('create', create_sanctionedoan_view, name='create')
]
