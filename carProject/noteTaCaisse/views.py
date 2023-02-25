from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Cars, Vote
from .forms import VoteForm
from django.db import models
from django.db import connection
from django.urls import reverse

# Create your views here.

def car_list(request):
    cars = Cars.objects.all()
    return render(request, 'noteTaCaisse/accueil.html', {'cars': cars})

@login_required
def car_detail(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    vote = None
    # Get the current user's vote for this car, if it exists
    try:
        vote = Vote.objects.get(car=car, user=request.user)
    except Vote.DoesNotExist:
        pass    
    if request.method == 'POST':
        # Get the value of the vote from the form submission
        vote_value = request.POST.get('vote')
        if vote_value is not None:
            try:
                vote_value = int(vote_value)
            except ValueError:
                pass
            else:
                if vote is None:
                    # Create a new vote
                    vote = Vote.objects.create(car=car, user=request.user, value=vote_value, date_created=timezone.now())
                else:
                    # Update the existing vote
                    vote.value = vote.value + vote_value
                    vote.date_created = timezone.now()
                    vote.save()
    # Calculate the total vote count for the car
    total_vote = Vote.objects.filter(car=car).aggregate(total=models.Sum('value'))['total'] or 0
    car.total_vote = total_vote
    car.save()
    form = VoteForm() if vote is None else VoteForm(initial={'value': vote.value})
    return render(request, 'noteTaCaisse/car_detail.html', {'car': car, 'form': form})

def reset_vote_count_view(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    Vote.objects.filter(car = car).update(value = 0)
    return redirect('car_detail', car_id=car.id)