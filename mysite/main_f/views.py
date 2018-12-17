from django.shortcuts import render


def main_f(request):
    return render(request, 'main_f/main_f.html')
