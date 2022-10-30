from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *

# Create your views here.
def djangoforms(request):
    NF=NameForm()
    d={'form':NF}
    if request.method=='POST':
        forms_data=NameForm(request.POST)
        if forms_data.is_valid():
            #return HttpResponse(str(forms_data.cleaned_data))
            n=forms_data.cleaned_data['name']
            a=forms_data.cleaned_data['age']
            p=forms_data.cleaned_data['password']
            d1={'a':a,'n':n,'p':p}
            return render(request,'data.html',d1)
    return render(request,'django_forms.html',d)


def insert_topic(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        form1_data=TopicForm(request.POST)
        if form1_data.is_valid():
            tn=form1_data.cleaned_data['topic_name']
            dt=form1_data.cleaned_data['date']
            T=Topic.objects.get_or_create(topic_name=tn,date=dt)[0]
            T.save()
            return HttpResponse('Ínserted values successfully')
    return render(request,'insert_topic.html', d)