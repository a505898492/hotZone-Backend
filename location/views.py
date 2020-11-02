from location.serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from location.models import Location
from rest_framework import status
import requests


class LocationList(APIView):

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)  
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchList(APIView):

    def get(self, request):
        geoDataList = requests.get('https://geodata.gov.hk/gs/api/v1.0.0/locationSearch', params=request.GET)
        if geoDataList.status_code == 200:
            return Response(geoDataList.json())
        return Response(status=status.HTTP_400_BAD_REQUEST)