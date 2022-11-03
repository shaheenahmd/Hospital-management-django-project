from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import departments,doctors

# Create your views here.

def index(request):
    return render(request, 'index.html')
        
def about(request):
   return render(request, 'about.html')

def booking(request):
     return render(request, 'booking.html')

def doctors(request):
    dict_docs={ 'doctors':doctors.objects.all() }
    return render(request, 'doctors.html', dict_docs)
    

def department(request):
    dict_dep = {'dept':departments.objects.all()}
    return render(request, 'department.html', dict_dep)

def contact(request):
    return render(request, 'contact.html')


