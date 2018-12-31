from django.shortcuts import render
from .forms import NameForm
from django.shortcuts import HttpResponse


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid:
            return HttpResponse ('/thanks/')
    else:
        form = NameForm()
    return render(request, 'main_f/main_f.html', context={'form': form})
