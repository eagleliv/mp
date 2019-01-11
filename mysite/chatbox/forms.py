from django import forms

class ChatForm(forms.Form):
    chat_text = forms.CharField(widget = forms.Textarea)
