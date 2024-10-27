from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.results, name='results'),
    path('results/details/<int:id>', views.details, name='details')
]