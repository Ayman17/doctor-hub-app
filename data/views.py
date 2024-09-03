from django.shortcuts import render
from .models import Doctors
from django.views.generic.list import ListView

# Create your views here.

class DoctorsData(ListView):
    model = Doctors
    template_name = 'home_page/index.html'
    context_object_name = 'doctors'

# class SearchDoctorsData(ListView):
#     model = Doctors
#     template_name = 'home_page/index.html'
#     context_object_name = 'doctors'

#     def get_queryset(self):
#         query = self.request.GET.get( )
#         return Doctors.objects.filter(name__icontains=query)
    
def SearchDoctorsData(request):
    return render(request, 'home_page/index.html', {'test': True})