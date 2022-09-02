from rest_framework import serializers
from .models import State, LocalGovenment, Hospital, Country



class HospitalSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"



class LocalSerialzer(serializers.ModelSerializer):
    class Meta:
        model = LocalGovenment
        fields = "__all__"



class StateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"