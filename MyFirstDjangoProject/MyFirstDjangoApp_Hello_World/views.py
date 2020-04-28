from django.shortcuts import render
from django.http import HttpResponse
from MyFirstDjangoApp_Hello_World.models import Topic,AccessRecord,Webpage

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    datedicts = {"access_records":webpages_list}
    return render(request, 'MyFirstDjangoApp_Hello_World/index.html' , context=datedicts)

