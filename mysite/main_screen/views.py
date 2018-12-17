from django.shortcuts import render


def m_scr(request):
    return render (request, 'main_screen/main_screen.html')
