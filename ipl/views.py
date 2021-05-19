import random

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import TeamForm, PlayerForm
from .models import Team, Player, Points, Match
from django.db import connection

# Create your views here.


def teams(request):
    # team = get_object_or_404(Team)
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "ipl/teams_list.html", {"teams": TeamForm()})
    else:
        form = TeamForm()
        return render(request, "ipl/teams_list.html", {"teams": form})


def teams_list(request):
    ipl_teams = Team.objects.all()
    print(ipl_teams)
    return render(request, 'ipl/teams.html', {"team": ipl_teams})


def delete_team(request, team_id):
    obj = get_object_or_404(Team, pk=team_id)
    obj.delete()
    ipl_teams = Team.objects.all()
    return render(request, 'ipl/teams.html', {"team": ipl_teams})


def player(request):
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "ipl/player_data.html", {"player": PlayerForm()})
    else:
        form = PlayerForm()
        return render(request, "ipl/player_data.html", {"player": form})


def team_details(request):
    team = Team.objects.all()
    return render(request, "ipl/team_details.html", {"team": team})


def team_players(request, team_id):
    team = Team.objects.get(team_id=team_id)
    players = Player.objects.filter(ipl_team=team)
    print(players)
    print(team)
    return render(request, "ipl/team_players.html", {"players": players, "team": team})


def player_details(request, player_id):
    # import pdb
    # pdb.set_trace()
    team_player = Player.objects.get(player_id=player_id)
    print(team_player)
    return render(request, "ipl/player_details.html", {"player": team_player})


def matches(request):
    all_teams = Team.objects.all()
    team1 = random.choice(all_teams)
    ex = all_teams.exclude(team_name=team1.team_name)
    team2 = random.choice(ex)
    winner = random.choice((team1, team2))
    win_tm, flag = Points.objects.get_or_create(team=winner)
    win_tm.played += 1
    win_tm.won += 1
    win_tm.points += 2
    win_tm.save()
    Match.objects.create(team1=team1, team2=team2, result=winner)
    if team1.team_name == win_tm.team.team_name:
        l_team = team2
    else:
        l_team = team1
    loss_tm, flag = Points.objects.get_or_create(team=l_team)
    loss_tm.played += 1
    loss_tm.lost += 1
    loss_tm.points += 0
    loss_tm.save()
    return render(request, "ipl/matches.html", {"win": win_tm, "loss": loss_tm, "teams": all_teams})


def total_matches(request):
    total = Match.objects.all()
    return render(request, "ipl/match_list.html", {"matches": total})


def points(request):
    point = Points.objects.all()
    print(point)
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM ipl_points ORDER BY points''')
    return render(request, "ipl/points_table.html", {"points": point})
