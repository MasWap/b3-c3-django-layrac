from django.urls import path
from .views import register, index, ecoles_view, eleves_view, reservation, mentions, contenu
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name="index"),
    path('ecoles/', ecoles_view, name="ecoles"),
    path('eleves/', eleves_view, name="eleves"),
    path('reservation/', reservation, name="reservation"),
    path('mentions/', mentions, name="mentions"),
    path('contenu/', contenu, name="contenu"),
    path('accounts/register', register, name="register"),
]