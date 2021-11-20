from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import *
# from .filters import *


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all().order_by('-id')
    serializer_class = AirplaneSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_class = AirplaneFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetAirplaneSerializer
        return self.serializer_class
