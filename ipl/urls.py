from . import views
from django.urls import path

app_name = 'ipl'

urlpatterns = [
    path('players/', views.players, name='players'),
    path('create/', views.create, name='create'),


]