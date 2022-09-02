from medicloc.models import State, LocalGovenment, Hospital, Country
from rest_framework import viewsets, permissions
from .serializers import LocalSerialzer, HospitalSerialzer, StateSerialzer, CountrySerializer

# we create the viewsets in the api file

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HospitalSerialzer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = LocalGovenment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocalSerialzer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StateSerialzer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CountrySerializer