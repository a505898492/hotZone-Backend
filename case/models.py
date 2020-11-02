from django.db import models
from patient.models import Patient
from virus.models import Virus


class Case(models.Model):
    LOCAL_OR_IMPORTED = [
        ('Local', 'Local'),
        ('Imported', 'Imported')
    ]

    objects = models.Manager()
    case_number = models.CharField(max_length=20) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    date_confirmed = models.DateField()
    local_or_imported = models.CharField(max_length=10, choices=LOCAL_OR_IMPORTED, default='Local')

    def __str__(self):
        return f"{self.case_number}: {self.patient} ({self.virus})"
