from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import *

FIXTURES = [
    "airline.airplane.json",
]


class AirplanAPITests(APITestCase):
    fixtures = FIXTURES

    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_airplan_list(self):
        url = reverse('airline:airline_v1:airplane-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(len(response_data), 1)

    def test_create_airplan(self):
        # Create new airplan using airplan api
        url = reverse('airline:airline_v1:airplane-list')
        data = {
            "liters": 200,
            "airplane_id": 4,
            "passengers": 20
        }

        response = self.client.post(url, data, format='json')
        # Created new airplan and now we are checking its status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 2)

        response_data = response.json()
        url = reverse('airline:airline_v1:airplane-detail', kwargs={'pk': response_data['id']})
        response = self.client.get(url, format='json')

        # get airplan and now we are checking its status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        # checking airplan dynamic value
        self.assertEqual(response_data['fuel_consumption_per_minute'], 3.24)
        self.assertEqual(response_data['maximum_minutes_to_fly'], 246.91)
