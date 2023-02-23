from django.urls import path
from .views import register, index, ecoles, eleves

urlpatterns = [
    path('', index, name="index"),
    path('ecoles/', ecoles, name="ecoles"),
    path('eleves/', eleves, name="eleves"),
    path('accounts/register', register, name="register"),
]