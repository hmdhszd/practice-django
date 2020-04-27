from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_data" : "Hi! This is my inserted data from my_dict in Views.py file  in first_app"}
    return render(request, "first_app/index.html" , context=my_dict)