from rest_framework import serializers
from .models import State, LocalGovenment, Hospital



class HospitalSerialzer(serializers.ModelSerializers):
    class Meta:
        model = Hospital
        fields = "__all__"



class LocalSerialzer(serializers.ModelSerializers):
    class Meta:
        model = LocalGovenment
        fields = "__all__"



class StateSerialzer(serializers.ModelSerializers):
    class Meta:
        model = State
        fields = "__all__"