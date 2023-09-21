from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def authentification(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_addEntreprise')
        else:
            messages.error(request, "Ce compte n'existe pas !")
    return render(request, 'app_authentification/authentification.html')

def deconnexion(request):
    logout(request)
    return redirect('view_authentification')
