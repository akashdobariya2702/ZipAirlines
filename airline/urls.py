# python library

# django library
from django.conf.urls import url, include

urlpatterns = [
	url(r'^v1/', include(('airline.v1.urls', 'airline_v1'), namespace='airline_v1')),
]
