from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("Home Page")

def About(request):
    return HttpResponse("About Page")

def Contact(request):
    return HttpResponse("Contact Page")
