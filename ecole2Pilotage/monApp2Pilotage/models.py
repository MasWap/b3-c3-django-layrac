from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Ecoles(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    since = models.PositiveIntegerField()
    students = models.IntegerField(default=0)
    image = models.ImageField(upload_to='ecoles/', default='auto-ecole1.png')
    
class Eleves(models.Model):
    GENDER_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('N/A', 'Non-genré'),
    ]   
    firstname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    date_register = models.DateField()

class Inscription(models.Model):
    ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleves, on_delete=models.CASCADE)
    date_inscription = models.DateField()
    

    def __str__(self):
        return self.name
