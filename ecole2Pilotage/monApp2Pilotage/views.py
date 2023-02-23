from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def index(request):
    return render(request, 'monApp2Pilotage/accueil.html')

def ecoles(request):
    return render(request, 'monApp2Pilotage/liste_ecoles.html')

def eleves(request):
    return render(request, 'monApp2Pilotage/liste_eleves.html')

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
