from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Model_PME
from .producer import publish_message


def addUser(request):
    if request.method == "POST":
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password2 != password1:
            messages.error(request, "Mot de passe incorrect !")
        else:
            username = f"{lastname}@{password2}"
            print(username, lastname, firstname, password1, password2)
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce compte existe déjà !")
            else:
                user = User.objects.create_user(username=username, last_name=lastname, first_name=firstname, password=password2)
                # Envoi du message
                message = {
                    'username': username,
                    'lastname': lastname, 
                    'firstname':firstname,
                    'password':password2
                }
                publish_message(message)
                if user:
                    messages.success(request, "Utilisateur créé avec succès !")
                else:
                    messages.error(request, "Erreur de création !")
    
    context = {
        'users':User.objects.filter(is_superuser=False)
    }
    
    return render(request, 'app_admin/add_user.html', context)

@login_required
def listEntreprise(request):
    context = {
        'entreprises': Model_PME.objects.all(),
        'totalEntreprise': Model_PME.objects.all().count(),
        'regulationEntreprise': Model_PME.objects.filter(regulation='conforme').count(),
        'activityEntreprise': Model_PME.objects.filter(activity=True).count(),
    }
    return render(request, "app_admin/list_entreprise.html", context)