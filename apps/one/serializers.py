from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from apps.one.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
