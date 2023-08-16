from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def doar(request):
    return render(request, "app/doar.html")