from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Ecoles, Inscription, Eleves
from .forms import LoginForm, UserForm

# Create your views here.

def ecoles_view(request):
    ecoles = Ecoles.objects.all()
    context = {'ecoles': ecoles}
    return render(request, 'monApp2Pilotage/liste_ecoles.html', context)


def eleves_view(request):
    inscriptions = Inscription.objects.all()
    context = {'inscriptions': inscriptions}
    return render(request, 'monApp2Pilotage/liste_eleves.html', context)

def eleve_view(request, id):
    eleve = get_object_or_404(Eleves, id=id)
    inscriptions = Inscription.objects.filter(eleve=eleve)
    return render(request, 'monApp2Pilotage/eleve.html', {'eleve': eleve, 'inscriptions': inscriptions})

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
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
        profile_form = UserForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

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
