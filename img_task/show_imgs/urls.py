from django.urls import path
from .views import index

urlpatterns = [
    path('cars/', index, name = 'cars'),
]