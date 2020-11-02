from django.db import models
from patient.models import Patient


class Location(models.Model):
    objects = models.Manager()
    location = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()

    def __str__(self):
        return self.location


class LocationVisitHistory(models.Model):
    CATEGORY = [
        ('Residence', 'Residence'),
        ('Workplace', 'Workplace'),
        ('Visit', 'Visit')
    ]
    
    objects = models.Manager()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY, default='Visit')

    def __str__(self):
        return f"{self.location_id}"