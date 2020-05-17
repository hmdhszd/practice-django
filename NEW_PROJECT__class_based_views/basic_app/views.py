from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')



class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    



class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic injection data !'
        return context





# def index(request):
#     return render(request,'index.html')




# class CBView(View):
#     def get(self,request):
#         return HttpResponse('class based views are cool!')




