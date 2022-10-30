from socket import fromshare

from django import forms

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)
    date=forms.DateField()