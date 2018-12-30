from django.shortcuts import render
import os


def partners(request):
    files = os.listdir('static/img')
    dict = {}
    for file in files:
        dict['img/' + file] = file[:len(file)-4] + '.com'
    return render(request, 'partners/partners.html', context={'r':dict})
