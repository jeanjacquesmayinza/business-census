from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def authentification(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser :
                login(request, user)
                return redirect('view_list_entreprise')
        else:
            messages.error(request, "Ce compte n'existe pas !")
    return render(request, 'app_authentification/authentification.html')

def deconnexion(request):
    logout(request)
    return redirect('view_authentification')
