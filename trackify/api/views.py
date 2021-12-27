from django.shortcuts import render
from rest_framework import generics
from .serializers import TrackSerializer
from .models import Track
class TrackView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer