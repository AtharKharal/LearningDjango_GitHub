from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Athar you are in Django Django !")