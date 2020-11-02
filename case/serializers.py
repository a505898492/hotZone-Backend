from rest_framework import serializers
from case.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'patient_id', 'virus_id', 'case_number', 'date_confirmed', 'local_or_imported']