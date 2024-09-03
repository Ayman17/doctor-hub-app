from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return redirect('getDoctorsData')

def about(request):
    return render(request, 'home_page/about.html')