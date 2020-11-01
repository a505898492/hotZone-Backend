from django.db import models


class Location(models.Model):
    objects = models.Manager()
    location = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()

    def __str__(self):
        return self.location
