from django.shortcuts import render


def via(request):
    return render(request, 'via/via.html')
