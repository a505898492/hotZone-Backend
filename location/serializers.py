from rest_framework import serializers
from location.models import Location, LocationVisitHistory


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location', 'address', 'x_coord', 'y_coord']


class LocationVisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationVisitHistory
        fields = ['id', 'patient_id', 'location_id', 'date_from', 'date_to', 'category']