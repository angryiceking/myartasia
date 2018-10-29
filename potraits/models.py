from django.db import models

# Create your models here.

class Potrait(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    medium = models.CharField(max_length=150)
    description = models.TextField()
    size = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    image = models.ImageField(upload_to='potraits/')

    def __str__(self):
        return self.title