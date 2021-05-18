from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams, name="teams"),
    path("teams_list/", views.teams_list, name="teams_list"),
    path("<int:team_id>/delete/", views.delete_team, name="delete_team"),
    path("player/", views.player, name="player_data"),
    path("teams_details/", views.team_details, name="teams_list"),
    path("<int:team_id>/details/", views.team_players, name="team_players"),
    path("details/<int:player_id>/",views.player_details, name = "player_details"),
    path("matches/", views.matches, name = "matches"),
    path("points/", views.points, name = "points"),
]
