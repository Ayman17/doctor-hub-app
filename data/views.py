from django.shortcuts import render
from .models import Doctors
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# TODO: add login required for views
class DoctorsData(ListView):
    model = Doctors
    template_name = 'home_page/index.html'
    context_object_name = 'doctors'

class SearchDoctorsData(ListView):
    model = Doctors
    template_name = 'home_page/index.html'
    context_object_name = 'result_doctors'

    def get_queryset(self):
        queryset = super().get_queryset()
        area = self.request.GET.get('area')
        specialization = self.request.GET.get('specialization')

        if area:
            queryset = queryset.filter(area=area)
        if specialization:
            queryset = queryset.filter(specialization=specialization)

        return queryset.distinct()

class DoctorDetails(DetailView):
    model = Doctors
    template_name = 'data/doctor_details.html'
    context_object_name = 'doctor'