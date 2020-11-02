from django.db import models
from patient.models import Patient
from virus.models import Virus


class Case(models.Model):
    LOCAL_OR_IMPORTED = [
        ('Local', 'Local'),
        ('Imported', 'Imported')
    ]

    objects = models.Manager()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus_id = models.ForeignKey(Virus, on_delete=models.CASCADE)
    case_number = models.CharField(max_length=20)
    date_confirmed = models.DateField()
    local_or_imported = models.CharField(max_length=10, choices=LOCAL_OR_IMPORTED, default='Local')

    def __str__(self):
        return self.case_number
