from django.shortcuts import render

def chatdetails(request):
    return render(request, 'chatbox/chatbox.html')

def room(request, room_name):
    return render(request, 'chatbox/room.html')
