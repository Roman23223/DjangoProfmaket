from rest_framework import serializers

from .models import Work, Image, Address, Email, Telephone_number, Application



class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class WorkSerializers(serializers.ModelSerializer):
    images = ImageSerializers(many=True)

    class Meta:
        model = Work
        fields = "__all__"


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class TelephoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telephone_number
        fields = "__all__"


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"