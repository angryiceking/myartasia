from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.name