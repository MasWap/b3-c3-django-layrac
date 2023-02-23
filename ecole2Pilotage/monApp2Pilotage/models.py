from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ecoles(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    since = models.PositiveIntegerField()
    students = models.IntegerField(default=0)
    image = models.ImageField(upload_to='ecoles/', default='auto-ecole1.png')

    def __str__(self):
        return self.name

    def image_url(self):
        return f'{settings.MEDIA_URL}{self.image.name}'
