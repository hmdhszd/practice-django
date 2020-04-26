from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<H1> This is my second project and my second APP that returns a text in H1 tag </h1>")

def help(request):
    c = {'my_context' : 'This is the context from views.py'}
    return render(request, "MySecondDjangoApp_Return_HTML/help.html",context=c)