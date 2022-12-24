from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('model data is inserted in Modelform')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    form=WebpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('webpagemodel data is inserted in Modelform')
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    form=AccessrecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessrecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('AccessrecordsModel data is inserted successfull in ModelForm')
    return render(request,'insert_accessrecords.html',d)