from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
        
def about(request):
   return render(request, 'about.html')

def booking(request):
     return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def department(request):
    return render(request, 'department.html')

def contact(request):
    return render(request, 'contact.html')


