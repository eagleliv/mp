from django.shortcuts import render
from django.views.generic import View
from .forms import ChatForm


chat1 = []

class ChatDetails(View):
    def get(self, request):
        chat = ChatForm()
        return render(request, 'chatbox/chatbox.html', context = {'chat': chat})
    def post(self, request):
        chat = ChatForm()
        new_chat = ChatForm(request.POST)
        if new_chat.is_valid():
            chat1.append(new_chat.cleaned_data.get('chat_text'))
            return render(request, 'chatbox/chatbox.html', context = {'chat': chat, 'chat1': chat1})
