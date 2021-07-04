from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Area1Model, Area2Model

class Areas1Serilizer(serializers.ModelSerializer):

    class Meta:
        model = Area1Model
        fields = '__all__'

class Areas2Serilizer(serializers.ModelSerializer):

    class Meta:
        model = Area2Model
        fields = '__all__'
