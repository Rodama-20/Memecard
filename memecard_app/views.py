from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'memecard-app/index.html')

def about(request):
    return render(request, 'memecard-app/about.html')


