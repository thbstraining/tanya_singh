from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Concert, SeatingLayout, Reservation
from .serializers import ConcertSerializer, SeatingLayoutSerializer, ReservationSerializer


from datetime import datetime

class ConcertModelTestCase(TestCase):
    def setUp(self):
        self.concert_data = {
            'name': 'Test Concert',
            'date': datetime(2024, 7, 15, 10, 0, 0),
            'venue': 'Test Venue'
        }

    def test_create_concert(self):
        concert = Concert.objects.create(**self.concert_data)
        self.assertEqual(concert.name, self.concert_data['name'])
        self.assertEqual(concert.date.strftime('%Y-%m-%dT%H:%M:%SZ'), self.concert_data['date'].strftime('%Y-%m-%dT%H:%M:%SZ'))
        self.assertEqual(concert.venue, self.concert_data['venue'])


class ConcertSerializerTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Test Concert',
            'date': '2024-07-15T10:00:00Z',
            'venue': 'Test Venue'
        }
        self.invalid_data = {
            'name': '',
            'date': '2024-07-15T10:00:00Z',
            'venue': 'Test Venue'
        }

    def test_valid_serializer(self):
        serializer = ConcertSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        serializer = ConcertSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())



class ConcertViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('concert-list')
        self.valid_payload = {
            'name': 'Test Concert',
            'date': '2024-07-15T10:00:00Z',
            'venue': 'Test Venue'
        }
        self.invalid_payload = {
            'name': '',
            'date': '2024-07-15T10:00:00Z',
            'venue': 'Test Venue'
        }

    def test_create_concert(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_concert(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReservationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.concert = Concert.objects.create(
            name='Test Concert',
            date='2024-07-15T10:00:00Z',
            venue='Test Venue'
        )
        self.seating_layout = SeatingLayout.objects.create(
            concert=self.concert,
            section='A',
            seat_number='1',
            is_reserved=False
        )
        self.url = reverse('reservation-list')
        self.valid_payload = {
            'concert': self.concert.id,
            'seating_layout': self.seating_layout.id,
            'name': 'Test User',
            'email': 'test@example.com'
        }
        self.invalid_payload = {
            'concert': self.concert.id,
            'seating_layout': self.seating_layout.id,
            'name': '',
            'email': 'test@example.com'
        }

    def test_create_reservation(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_reservation(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_reservation_seat_already_reserved(self):
        # Reserve the seat first
        self.seating_layout.is_reserved = True
        self.seating_layout.save()

        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_reservation_invalid_seating_layout(self):
        invalid_payload = self.valid_payload.copy()
        invalid_payload['seating_layout'] = 9999  # Non-existing seating layout id

        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class SeatingLayoutViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('seatinglayout-list')
        self.valid_payload = {
            'concert': 1,  # Replace with a valid concert ID
            'section': 'A',
            'seat_number': '1',
            'is_reserved': False
        }
        self.invalid_payload = {
            'concert': 1,  # Replace with a valid concert ID
            'layout_name': 'Invalid Layout',  # Use an invalid field name
            'capacity': 100  # Use an invalid field name
        }

    def test_create_invalid_seating_layout(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
