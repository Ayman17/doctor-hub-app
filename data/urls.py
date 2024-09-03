from django.urls import path
from .views import *

urlpatterns = [
    path('get-doctors-data/', DoctorsData.as_view(), name='getDoctorsData'),
    path('search-doctors-data/', SearchDoctorsData, name='searchDoctorsData'),
]
