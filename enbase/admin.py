from django.contrib import admin
from .models import Game,GameDomain,GameType

admin.site.register(Game)
admin.site.register(GameDomain)
admin.site.register(GameType)