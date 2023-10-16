from django.db import models

# Create your models here.
from salons.models import Salon


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")
    salon = models.ManyToManyField(Salon)

    def __str__(self):
        return self.name
