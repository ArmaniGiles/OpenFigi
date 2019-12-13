from drf_braces.forms.serializer_form import SerializerForm
from rest_framework import serializers
from .models import Cusip

class CusipSerializers(serializers.Serializer):
    ticker = serializers.CharField(max_length=200) 
    name = serializers.CharField(max_length=200)
    marketSector = serializers.CharField(max_length=200)
    securityType = serializers.CharField(max_length=200)
    exchCode = serializers.CharField(max_length=200)

class MySerializerForm(SerializerForm):

    class Meta(object):
        serializer = CusipSerializers
