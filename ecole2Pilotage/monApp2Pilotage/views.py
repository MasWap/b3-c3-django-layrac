from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Ecoles, Inscription
from .forms import LoginForm

# Create your views here.

def ecoles_view(request):
    ecoles = Ecoles.objects.all()
    context = {'ecoles': ecoles}
    return render(request, 'monApp2Pilotage/liste_ecoles.html', context)


def eleves_view(request):
    inscriptions = Inscription.objects.all()
    context = {'inscriptions': inscriptions}
    return render(request, 'monApp2Pilotage/liste_eleves.html', context)

def index(request):
    return render(request, 'monApp2Pilotage/accueil.html')

def ecoles(request):
    return render(request, 'monApp2Pilotage/liste_ecoles.html')


def reservation(request):
    return render(request, 'monApp2Pilotage/liste_reservation.html')

def mentions(request):
    return render(request, 'monApp2Pilotage/mentions_legales.html')

def contenu(request):
    return render(request, 'monApp2Pilotage/contenu_site.html')

def register(request):
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes maintenant connecté.')
                return redirect('home')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Le formulaire est invalide.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
