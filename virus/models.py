from django.db import models


class Virus(models.Model):
    objects = models.Manager()
    virus_name = models.CharField(max_length=20)
    max_infectious_period = models.IntegerField()
    disease = models.CharField(max_length=20)

    def __str__(self):
        return self.virus_name
