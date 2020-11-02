from django.db import models


class Patient(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=120)
    identity_document_number = models.CharField(max_length=120)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
