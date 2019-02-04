from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import utils

class Game(View):
    def get(self, request):
        return render(request, 'game/game.html')
    def post(self, request):
        a = utils.Game_Utils()
        return render(request, 'game/game.html', context={'param': a.game(request)})
