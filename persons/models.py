from django.db import models


# Create your models here.

class Person(models.Model):
    image = models.ImageField(upload_to="image/")
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
