from django.http import JsonResponse
from .models import State, LocalGovenment, Country, Hospital
from django.forms.models import model_to_dict
from medicloc.serializers import CountrySerializer

# restframework imports
from rest_framework.response  import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Country.objects.all().order_by("?").first()

    # data = {}
    
    if instance:

        # intel = model_to_dict(instance, fields=["id", "name", "capital", "abbrv"])
        data = CountrySerializer(instance).data

    return Response(data)