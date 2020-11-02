from rest_framework import serializers
from location.models import Location, LocationVisitHistory


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location', 'address', 'x_coord', 'y_coord']


class LocationVisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationVisitHistory
        fields = ['id', 'case', 'location', 'date_from', 'date_to', 'category']


class LocationVisitHistoryListSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    x_coord = serializers.SerializerMethodField()
    y_coord = serializers.SerializerMethodField()

    class Meta:
        model = LocationVisitHistory
        fields = ['id', 'location', 'address', 'x_coord', 'y_coord', 'date_from', 'date_to', 'category']
    
    def get_location(self, obj):
        return obj.location.location
    
    def get_address(self, obj):
        return obj.location.address
    
    def get_x_coord(self, obj):
        return obj.location.x_coord
    
    def get_y_coord(self, obj):
        return obj.location.y_coord
    
