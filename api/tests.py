from rest_framework import status
from rest_framework.test import APITestCase
from django.core import mail
from django.conf import settings
from django.template import loader
from .models import Work, Image, Address, Email, Telephone_number, Application


class ModelTest(APITestCase):

    def test_model_work(self):
        self.work = Work.objects.create(
            title='test',
            content='test',
        )
        self.assertEqual(self.work.title, 'test')
        self.assertEqual(self.work.content, 'test')

    def test_model_image(self):
        self.image = Image.objects.create(
            title='test',
        )
        self.assertEqual(self.image.title, 'test')

    def test_get_list_address(self):
        self.address = Address.objects.create(
            address='test',
        )
        self.assertEqual(self.address.address, 'test')

    def test_get_list_email(self):
        self.email = Email.objects.create(
            email='test@mail.ru',
            title='test',
        )
        self.assertEqual(self.email.email, 'test@mail.ru')
        self.assertEqual(self.email.title, 'test')

    def test_get_list_telephone(self):
        self.telephone_number = Telephone_number.objects.create(
            number='test',
        )
        self.assertEqual(self.telephone_number.number, 'test')

    def test_get_list_application(self):
        self.application = Application.objects.create(
            size="test",
            product_time="test",
            sender_name="test",
            number="test",
            email="test@mail.ru",
            comment="test"
        )
        self.assertEqual(self.application.size, 'test')
        self.assertEqual(self.application.product_time, 'test')
        self.assertEqual(self.application.sender_name, 'test')
        self.assertEqual(self.application.number, 'test')
        self.assertEqual(self.application.email, 'test@mail.ru')
        self.assertEqual(self.application.comment, 'test')


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

class sendMailTest(APITestCase):

    def test_send_email(self):
        mail.send_mail(
            'Title message', 
            'Body message',
            settings.EMAIL_HOST_USER, 
            ['roma_chepiga@mail.ru'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Title message')
        self.assertEqual(mail.outbox[0].body, 'Body message')