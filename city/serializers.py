from rest_framework import serializers
from .models import City


# class CityModel:
#     def __init__(self,name):
#         self.name = name
#

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return City.objects.create(**validated_data)

