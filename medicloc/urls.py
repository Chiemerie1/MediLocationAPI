from django.db import router
from rest_framework import routers
from .api import HospitalViewSet, LocalViewSet, StateViewSet



router = routers.DefaultRouter()
router.register("api/hospitals", HospitalViewSet, "hospitals")
router.register("api/local-government", LocalViewSet, "local")
router.register("api/state", StateViewSet, "state")


urlpatterns = router.urls