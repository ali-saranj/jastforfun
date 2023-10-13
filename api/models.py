from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Salon(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    user = models.ManyToManyField(User)
    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
