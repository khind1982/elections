from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("results/", views.results, name="results"),
    path("results/details/<int:id>", views.details, name="details"),
    path("fruits/", views.fruits, name="fruits"),
]
