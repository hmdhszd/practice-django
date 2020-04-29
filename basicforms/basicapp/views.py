from django.shortcuts import render
from . import forms

# Create your views here.
def index(resuest):
    return render(resuest, 'basicapp/index.html')



def form_name_view(request):
    form = forms.FormName()
    return render(request, 'basicapp/form_page.html', {'form':form})