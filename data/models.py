from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_images/', default='media/doctor_images/doctor.jpg')

    def __str__(self):
        return self.name