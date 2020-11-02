from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from location.serializers import LocationVisitHistorySerializer
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


class CaseHistory(APIView):

    def get(self, request, pk):
        histories = LocationVisitHistory.objects.filter(case=pk)
        serializer = LocationVisitHistorySerializer(histories, many=True)  
        return Response(serializer.data)