from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ndk = 'This is the index page'
    return render(request, 'rango/index.html', {'message': ndk})

def about(request):
    return render(request, 'rango/about.html', {'message': 'This is the about page'})
