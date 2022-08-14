from rest_framework import serializers
from .models import State, LocalGovenment, Hospital



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