from django.urls import path
from . import views

urlpatterns = [
    path("states/", views.get_states),
    path("cities/", views.get_cities),
    path("crops/", views.get_crops),
    path("regions/", views.get_regions),
    path("weather/", views.get_weather),
    path("soil/", views.get_soil),
    path("health/", views.get_health),
    path("dashboard/", views.get_dashboard),
]
