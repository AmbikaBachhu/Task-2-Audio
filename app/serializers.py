from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    audio_file = serializers.FileField(use_url=True)

    class Meta:
        model = Song
        fields = ['id','title','duration','audio_file']
