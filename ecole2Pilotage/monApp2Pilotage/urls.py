from django.urls import path
from .views import register, index, ecoles, eleves, reservation, mentions, contenu

urlpatterns = [
    path('', index, name="index"),
    path('ecoles/', ecoles, name="ecoles"),
    path('eleves/', eleves, name="eleves"),
    path('reservation/', reservation, name="reservation"),
    path('mentions/', mentions, name="mentions"),
    path('contenu/', contenu, name="contenu"),
    path('accounts/register', register, name="register"),
]