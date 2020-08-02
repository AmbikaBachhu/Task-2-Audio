from django.shortcuts import render
from .models import Song
from rest_framework import viewsets
from .serializers import SongSerializer
from rest_framework import filters


# Create your views here.
class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_fields = ('duration',)
    ordering =('duration',)
