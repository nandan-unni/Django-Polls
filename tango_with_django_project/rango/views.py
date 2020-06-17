from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page loaded <br/> <a href = '\\about'>About</a>")

def about(request):
    return HttpResponse("This page gives the information about Rango App. <br/> <a href='\\'>Home</a>")