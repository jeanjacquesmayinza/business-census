from django.shortcuts import render
from .models import Model_PME
from django.contrib import messages
from .producer import *

def addEntreprise(request):
    if request.method == "POST":
        name = request.POST.get('name')
        fullAddress = request.POST.get('fullAddress')
        entrepreneur = request.POST.get('entrepreneur')
        creationDate = request.POST.get('creationDate')
        regulation = request.POST.get('regulation')
        NumberOfEmployees = int(request.POST.get('NumberOfEmployees'))
        activity = request.POST.get('activity')
        print(name, fullAddress, entrepreneur, creationDate, regulation, NumberOfEmployees, activity)
        pme = Model_PME.objects.create(
            name=name,
            fullAddress=fullAddress,
            entrepreneur=entrepreneur,
            creationDate=creationDate,
            NumberOfEmployees=NumberOfEmployees,
            regulation=regulation,
            activity=activity
        )
        pme.save()
        if pme:
            messages.success(request, "Enregistrement réussie")
            message = {
                'name': name,
                'fullAddress': fullAddress,
                'entrepreneur': entrepreneur,
                'creationDate':creationDate,
                'NumberOfEmployees': NumberOfEmployees,
                'regulation': regulation,
                'activity': activity
            }
            publish_message(message)
        else:
            messages.error(request, "Erreur d'enregistrement")
    context = {
        'entreprises': Model_PME.objects.all(),
    }

    return render(request, 'app_agent/add_entreprise.html', context)