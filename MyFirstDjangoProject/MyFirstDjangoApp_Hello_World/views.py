from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    mydict = {'insert_me':'hello im the INSERT ME   from  Views.py'}
    return render(request, 'MyFirstDjangoApp_Hello_World/index.html' , context=mydict)

