from django.db import models

# Create your models here.
from salons.models import Salon


class Category(models.Model):
    name = models.CharField(max_length=100)
    salon = models.ManyToManyField(Salon)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.name
