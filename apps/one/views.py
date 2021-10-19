from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from .models import Event

from .serializers import EventSerializer

# Create your views here.

class EvenAPI(ListCreateAPIView):
    serializer_class = EventSerializer
    serializer_class = EventSerializer
    queryset = Event.objects.all()


# class CreateEventAPIView(CreateAPIView):
#     serializer_class = EventSerializer


# class ListEventAPIView(ListAPIView):
#     serializer_class = EventSerializer
#     queryset = Event.objects.all()
