from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.title
