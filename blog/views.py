from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

def home(request): 
    return render(request, 'blog/home.html')
def about(request):    
    return render(request , 'blog/about.html')
    

# Create your views here.
