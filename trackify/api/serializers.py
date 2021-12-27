from rest_framework import serializers
from .models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'code', 'artist', 'name', 'genre', 'album_image_url', 'preview_url', 'created_at')