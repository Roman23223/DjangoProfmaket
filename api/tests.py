from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
from django.core import mail
from django.conf import settings
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

    def setUp(self):
        self.client = Client()
        self.work = Work.objects.create(
            title='test',
            content='test'
        )
        self.url = f'/api/work/{self.work.pk}/'
        Image.objects.create(
            title='test',
        )
        Address.objects.create(
            address='test',
        )
        Email.objects.create(
            email='test@mail.ru',
            title='test',
        )
        Telephone_number.objects.create(
            number='test',
        )
    
    def test_get_all_work(self):
        response = self.client.get('/api/work/')
        work = Work.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(work))

    def test_get_one_work(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), 'test')

    def test_get_all_image(self):
        response = self.client.get('/api/image/')
        image = Image.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(image))

    def test_get_all_address(self):
        response = self.client.get('/api/address/')
        address = Address.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(address))

    def test_get_all_email(self):
        response = self.client.get('/api/email/')
        email = Email.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(email))

    def test_get_all_number(self):
        response = self.client.get('/api/telephone/')
        number = Telephone_number.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(number))

    def test_create_application(self):
        url = '/api/application/create/'
        
        data = {
            "size": "test",
            "product_time": "test",
            "sender_name": "test",
            "number": "test",
            "email": "test@mail.ru",
            "comment": "test"
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 1)
        
        application = Application.objects.first()
        self.assertEqual(application.size, 'test')
        self.assertEqual(application.product_time, 'test')
        self.assertEqual(application.sender_name, 'test')
        self.assertEqual(application.number, 'test')
        self.assertEqual(application.email, 'test@mail.ru')
        self.assertEqual(application.comment, 'test')
    

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