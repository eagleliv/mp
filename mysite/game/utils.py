from django.shortcuts import render

class Game_Utils():
    def game(self, request):
        if request.POST:
            h = request.POST.get('hhh')
            print(h)
        return h
