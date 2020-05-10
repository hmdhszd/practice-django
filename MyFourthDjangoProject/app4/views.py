from django.shortcuts import render
# from app4.models import User
from app4.forms import NewUserForm
# Create your views here.



def index(requeset):
    return render(requeset, 'app4/index.html',)


def users(request):
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("error form is not valid")

    return render(request,"app4/users.html",{'form':form})
    