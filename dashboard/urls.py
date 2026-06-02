from django.urls import path
from . import views

urlpatterns = [
    path("states/", views.get_states),
    path("cities/", views.get_cities),
    path("crops/", views.get_crops),
]