from rest_framework import serializers
from virus.models import Virus


class VirusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virus
        fields = ['id', 'virus_name', 'max_infectious_period', 'disease']
