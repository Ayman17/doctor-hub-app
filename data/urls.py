from django.urls import path
from . import views

urlpatterns = [
    path('get_doctors_data/', views.getData, name='getDoctorsData'),
]
