from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def home(request):
    datas_emprunteur = Emprunteur.objects.all()

    context = {
        'datas_emprunteur': datas_emprunteur
    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_emprunteur = Emprunteur(first_name=first_name, last_name=last_name)
        new_emprunteur.save()

    return render(request, 'home.html', context)


def delete_emprunteur(request, id):
    if request.method == 'POST':
        pi = Emprunteur.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_emprunteur(request, id):
    if request.method == 'POST':
        pi = Emprunteur.objects.get(pk=id)
        if not pi.bloque:
            pi.bloque = True
        else:
            pi.bloque = False
        pi.save()
        return HttpResponseRedirect('/')
