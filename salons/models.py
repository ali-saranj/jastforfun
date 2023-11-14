from django.db import models

from images.models import Image
# Create your models here.
from persons.models import Person


class Salon(models.Model):
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    person = models.ManyToManyField(Person)
    location = models.CharField(max_length=500)
    latitude = models.CharField(max_length=100,blank=True)
    longitude = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    isSpecial = models.BooleanField(default=False)

    def __str__(self):
        return self.name
