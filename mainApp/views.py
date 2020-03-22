from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')

def registr(request):
    return render(request, 'mainApp/registration.html')