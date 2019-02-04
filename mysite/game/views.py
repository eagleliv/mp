from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

def game(request):
    if request.POST:
        h = request.POST.get('hhh')
        print(h)
    return render(request, 'game/game.html')
# Create your views here.
