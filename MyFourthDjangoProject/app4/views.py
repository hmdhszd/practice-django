from django.shortcuts import render
from app4.models import User
# Create your views here.



def index(requeset):
    return render(requeset, 'app4/index.html',)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'app4/users.html', context=user_dict)