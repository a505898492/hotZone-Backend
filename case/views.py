from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from location.serializers import LocationSerializer, LocationVisitHistorySerializer, LocationVisitHistoryListSerializer
from case.serializers import CaseSerializer
from location.models import LocationVisitHistory
from case.models import Case
import requests


class CaseList(APIView):

    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)  
        return Response(serializer.data)


class CaseDetail(APIView):

    def get_object(self, pk):
        case = get_object_or_404(Case, pk=pk)
        return case

    def get(self, request, pk):
        case = self.get_object(pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)


class CaseLocationHistory(APIView):

    def get(self, request, pk):
        histories = LocationVisitHistory.objects.filter(case=pk)
        serializer = LocationVisitHistoryListSerializer(histories, many=True)  
        return Response(serializer.data)
    
    def post(self, request, pk):
        # Add location Data
        location_data = {
            "location": request.data['location'],
            "address": request.data['address'],
            "x_coord": request.data['x_coord'],
            "y_coord": request.data['y_coord'],
        }

        location_serializer = LocationSerializer(data=location_data)
        
        if location_serializer.is_valid():
            location_serializer.save()
        else:
            return Response(location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Add Case location visit history Data
        location_history_data = {
            'case': pk, 
            'location': location_serializer.data['id'], 
            'date_from': request.data['date_from'], 
            'date_to': request.data['date_to'], 
            'category': request.data['category']
        }
        location_history_serializer = LocationVisitHistorySerializer(data=location_history_data)

        if location_history_serializer.is_valid():
            location_history_serializer.save()
            return Response(location_history_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(location_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
