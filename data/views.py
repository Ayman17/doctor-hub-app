from django.shortcuts import render
from .models import Doctors
from django.views.generic.list import ListView

# Create your views here.

class DoctorsData(ListView):
    model = Doctors
    template_name = 'home_page/index.html'
    context_object_name = 'doctors'