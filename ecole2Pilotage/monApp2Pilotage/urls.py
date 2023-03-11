from django.urls import path
from .views import register, index, ecoles_view, eleves_view, eleve_view, reservation, mentions, contenu
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name="index"),
    path('ecoles/', ecoles_view, name="ecoles"),
    path('eleves/', eleves_view, name="eleves"),
    path('eleve/<int:id>/', eleve_view, name='eleve_view'),
    path('reservation/', reservation, name="reservation"),
    path('mentions/', mentions, name="mentions"),
    path('contenu/', contenu, name="contenu"),
    path('accounts/register', register, name="register"),
]