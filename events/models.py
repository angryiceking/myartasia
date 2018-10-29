from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    organizer = models.CharField(max_length=150)
    date = models.DateTimeField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.name