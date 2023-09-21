from django.urls import path
from .views import *

urlpatterns = [
    path("add_user", addUser, name="view_add_user"),
    path("list_entreprise", listEntreprise, name="view_list_entreprise")
]
