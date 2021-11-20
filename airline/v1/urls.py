# python library

# django library
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# project library
from .views import *

# app_name = 'airline'

router = DefaultRouter()

# app urls
router.register(r'airplane', AirplaneViewSet, basename='airplane')

urlpatterns = [
    url(r'^', include(router.urls)),
]
