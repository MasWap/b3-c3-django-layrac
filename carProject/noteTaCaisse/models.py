from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    hp = models.DecimalField(decimal_places=1, max_digits=4)
    version = models.CharField(max_length=50)
    total_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Vote(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=[(i, i) for i in range(-5, 6)], default=0)
    date_created = models.DateTimeField(auto_now_add=True)
