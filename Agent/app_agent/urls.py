from django.urls import path
from .views import *

urlpatterns = [
    path('add_entreprise', addEntreprise, name='view_addEntreprise'),
]