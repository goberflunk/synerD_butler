from django.shortcuts import render

def index(request):
    return render(request, 'SolarPV/wireframe1.html')

def register(request):
    return render(request, 'SolarPV/register.html')

def dashboard(request):
    return render(request, 'SolarPV/dashboard.html')
