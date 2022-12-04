from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'memecard_app/index.html')

def about(request):
    return render(request, 'memecard_app/about.html')


