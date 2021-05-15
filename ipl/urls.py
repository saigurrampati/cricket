from . import views
from django.urls import path

app_name = 'ipl'

urlpatterns = [
    path('players/', views.players, name='players'),
    path('create/', views.create, name='create'),
    path('', views.home, name='home'),
    path('<int:player_id>/details/', views.details, name='details'),
    path('teams/', views.teams, name='teams'),
    path('franchise/', views.franchise, name='franchise'),
    path('<int:team_id>/team_details/', views.team_details, name='team_details')







]