from rest_framework import serializers
from case.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'patient', 'virus', 'case_number', 'date_confirmed', 'local_or_imported']

class CaseListSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    patient_id_number = serializers.SerializerMethodField()
    patient_birth = serializers.SerializerMethodField()
    virus_name = serializers.SerializerMethodField()
    disease = serializers.SerializerMethodField()
    max_infectious_period = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = ['id', 'case_number', 'date_confirmed', 'local_or_imported', 
        'patient_name', 'patient_id_number', 'patient_birth', 'virus_name', 'disease', 
        'max_infectious_period']
    
    def get_patient_name(self, obj):
        return obj.patient.name

    def get_patient_id_number(self, obj):
        return obj.patient.identity_document_number

    def get_patient_birth(self, obj):
        return obj.patient.date_of_birth

    def get_virus_name(self, obj):
        return obj.virus.virus_name

    def get_disease(self, obj):
        return obj.virus.disease

    def get_max_infectious_period(self, obj):
        return obj.virus.max_infectious_period