from django.shortcuts import render


def via(request):
    dictadr = {'Адрес: ': 'Украина, Киев, Порика 7Б', 'Режим работы: ': 'Пн-пт: с 10:00 до 18:00, Сб: с 10:00 до 15:00', 'E-mail: ': 'Lyapiny@ukr.net', 'Тел: ': '+38(050)469-0727'}
    return render(request, 'via/via.html', context={'adr': dictadr})
