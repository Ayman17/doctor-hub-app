from django.urls import path
from .views import *

urlpatterns = [
    path('get-doctors-data/', DoctorsData.as_view(), name='getDoctorsData'),
    path('search-doctors-data/', SearchDoctorsData.as_view(), name='searchDoctorsData'),
    path('<int:pk>/', DoctorDetails.as_view(), name='doctorDetails')
]
