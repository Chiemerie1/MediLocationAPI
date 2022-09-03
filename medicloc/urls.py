from django.db import router
from rest_framework import routers
from .api import HospitalViewSet, LocalViewSet, StateViewSet, CountryViewSet

from django.urls import path
from . import views



# router = routers.DefaultRouter()
# router.register("api/hospitals", HospitalViewSet, "hospitals")
# router.register("api/local-government", LocalViewSet, "local")
# router.register("api/state", StateViewSet, "state")
# router.register("api/country", CountryViewSet, "country")


# urlpatterns = router.urls

urlpatterns = [
    path("", views.api_home)
]