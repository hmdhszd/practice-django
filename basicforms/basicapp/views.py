from django.shortcuts import render
from . import forms

# Create your views here.
def index(resuest):
    return render(resuest, 'basicapp/index.html')



def form_name_view(request):
    form = forms.FormName()
    
    
    
    
    
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
               
        if form.is_valid():
            print('validation successful')
            print(form.cleaned_data['name'])
            
    
    
    
    
    
    return render(request, 'basicapp/form_page.html', {'form':form})