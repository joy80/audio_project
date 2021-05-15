from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.

class Song(models.Model):
    song_name = models.CharField(max_length=100,blank=False,null=False)
    duration = models.IntegerField(blank=False,null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True,blank=False,null=False)

    def __str__(self):
        return self.song_name


class Podcast(models.Model):
    podcast_name = models.CharField(max_length=100,blank=False,null=False)
    host = models.CharField(max_length=100,blank=False,null=False)
    participants = ArrayField(models.CharField(max_length=100),blank=True,null=True,size=10)
    duration = models.IntegerField(blank=False,null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True,blank=False,null=False)

    def __str__(self):
        return self.podcast_name


class Audiobook(models.Model):
    audio_title = models.CharField(max_length=100,blank=False,null=False)
    author = models.CharField(max_length=100,blank=False,null=False)
    narrator = models.CharField(max_length=100,blank=False,null=False)
    duration = models.IntegerField(blank=False,null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.audio_title


