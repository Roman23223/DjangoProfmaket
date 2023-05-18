from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase
from .models import Work, Image, Address, Email, Telephone_number, Application


class ModelTest(APITestCase):

    def test_model_work(self):
        self.work = Work.objects.create(
            title='тест',
            content='тест',
        )

    def test_model_image(self):
        self.work = Image.objects.create(
            title='тест',
        )

    def test_get_list_address(self):
        self.work = Address.objects.create(
            address='тест',
        )

    def test_get_list_email(self):
        self.work = Email.objects.create(
            email='test@mail.ru',
            title='тест',
        )

    def test_get_list_telephone(self):
        self.work = Telephone_number.objects.create(
            number='тест',
        )

    def test_get_list_application(self):
        self.work = Application.objects.create(
            size="тест",
            product_time="тест",
            sender_name="тест",
            number="тест",
            email="test@mail.ru",
            comment="тест"
        )


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