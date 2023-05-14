from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Work, Image, Address, Email, Telephone_number, Application
from .serializers import WorkSerializers, ImageSerializers, AddressSerializers, EmailSerializers, TelephoneSerializers, ApplicationSerializers


class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WorkOne(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EmailList(generics.ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TelephoneList(generics.ListAPIView):
    queryset = Telephone_number.objects.all()
    serializer_class = TelephoneSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers
