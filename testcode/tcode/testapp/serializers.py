from .models import *
from rest_framework import serializers

class ServerlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serverlist
        fields = '__all__'

        

