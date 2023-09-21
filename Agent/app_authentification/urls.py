from django.urls import path
from .views import *

urlpatterns = [
    path("", authentification, name="view_authentification"),
    path("deconnexion", deconnexion, name="view_deconnexion"),
]