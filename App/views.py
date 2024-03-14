from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from App.models import Patient
from django.contrib import messages

#Fonction qui mène au chemin de la page d'accueil
def frontend(request):
    return render(request, "frontend.html")


#Fonction qui te fait sortir de la page d'accueil
@login_required(login_url= "login")
def backend(request):
    return render(request, "backend.html")

#Fonction d'insertion de patient
@login_required(login_url= "login")
def add_patient(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('prename') and request.POST.get('phone') and request.POST.get('age') and request.POST.get('sexe') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.prename = request.POST.get('prename')
            patient.phone = request.POST.get('phone')
            patient.age = request.POST.get('age')
            patient.sexe = request.POST.get('sexe')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Le patient a été ajouté avec succès !")
            return redirect("/backend")
    else:
        return render(request, "add.html")
    
