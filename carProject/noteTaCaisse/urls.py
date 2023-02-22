from django.urls import path
from .views import reset_vote_count_view
from . import views

urlpatterns = [
    path('', views.car_list, name="car_list"),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
    path('reset_vote_count/<int:car_id>/', views.reset_vote_count_view, name='reset_vote_count'),
]