from django.shortcuts import render


def partners(request):
    return render(request, 'partners/partners.html')
