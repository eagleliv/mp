from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import utils

class Game(View):
    def get(self, request):
        a = utils.Hero()
        return render(request, 'game/game.html', context={'param': a.show_character()})
    def post(self, request):
        a = utils.Hero()
        return render(request, 'game/game.html', context={'param': a.your_move(request)})
