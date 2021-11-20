# python library

# django library
from rest_framework import serializers

from ..models import *


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'
        # exclude = ('id', )

    def validate(self, attrs):
        total_airplanes = Airplane.objects.all().count()
        if total_airplanes >= 10:
            raise serializers.ValidationError({"detail":"Can not add more than 10 airline"})
        return attrs



class GetAirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute = serializers.SerializerMethodField()
    maximum_minutes_to_fly = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = '__all__'

    def get_fuel_consumption_per_minute(self, obj):
        return obj.fuel_consumption_per_minute

    def get_maximum_minutes_to_fly(self, obj):
        return obj.maximum_minutes_to_fly
