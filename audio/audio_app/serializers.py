from rest_framework import serializers
from .models import Song, Podcast, Audiobook

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

    def validate(self, attrs):
        participants=attrs.get('participants')
        if len(participants)> 10:
            raise serializers.ValidationError({'participants':('Participants more than 10 is not allowed')})
        return super().validate(attrs)
        

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'