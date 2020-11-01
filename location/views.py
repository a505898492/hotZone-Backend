from rest_framework.generics import get_object_or_404
from location.serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from location.models import Location
from rest_framework import status
from django.http import Http404


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
