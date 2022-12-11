# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = f"Bonjour le monde !!!"
    return HttpResponse(message)
