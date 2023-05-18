from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ViewsTest(APITestCase):

    def test_get_list_work(self):
        url = '/api/work'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_image(self):
        url = '/api/image'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_address(self):
        url = '/api/address'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_email(self):
        url = '/api/email'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_telephone(self):
        url = '/api/telephone'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_application(self):
        url = '/api/application/create'
        data = {
            "size": "1 к 1000",
            "product_time": "1 месяц",
            "sender_name": "Заказчик",
            "number": "00000000000",
            "email": "zakazchik@mail.ru",
            "comment": "Тест"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)