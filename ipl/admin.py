from django.contrib import admin
from .models import Team, Player, Points, Match
# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Points)
admin.site.register(Match)

