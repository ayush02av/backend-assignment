from pyrsistent import field
from rest_framework import serializers
from database import models

class record_serializer(serializers.ModelSerializer):
    class Meta():
        model = models.record
        fields = '__all__'