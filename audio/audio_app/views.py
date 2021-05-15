from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import *

# Create your views here.

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            audio_data = JSONParser().parse(request)
            audio_type = audio_data.get('audioFileType')

            if audio_type and audio_type.lower() == 'song':
                serializer = SongSerializer(data=audio_data.get('audioFileMetadata'))
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif audio_type and audio_type.lower() == 'podcast':
                serializer = PodcastSerializer(data=audio_data.get('audioFileMetadata'))
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif audio_type and audio_type.lower() == 'audiobook':
                serializer = AudiobookSerializer(data=audio_data.get('audioFileMetadata'))
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'audioFileType':'audioFileType error'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'error':str(e)})
    return JsonResponse({'done':'success'})


@csrf_exempt
def delete(request, audioFileType, id):
    if request.method == 'POST':
        try:
            if audioFileType.lower() == 'song':
                song_obj = Song.objects.filter(id=id).first()
                if song_obj:
                    song_obj.delete()
                    return JsonResponse({'success':'deleted'}, status=status.HTTP_200_OK)
                else:
                   return JsonResponse({'failed':'detail not found'}, status=status.HTTP_400_BAD_REQUEST) 
            elif audioFileType.lower() == 'podcast':
                podcast_obj = Podcast.objects.filter(id=id).first()
                if podcast_obj:
                    podcast_obj.delete()
                    return JsonResponse({'success':'deleted'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'failed':'detail not found'}, status=status.HTTP_400_BAD_REQUEST)
            elif audioFileType.lower() == 'audiobook':
                audiobook_obj = Audiobook.objects.filter(id=id).first()
                if audiobook_obj:
                    audiobook_obj.delete()
                    return JsonResponse({'success':'deleted'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'failed':'detail not found'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'failed':'audioFileType missmatch'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error':str(e)})
    return JsonResponse({'done':'success'})
    

@csrf_exempt
def update(request, audioFileType, id):
    if request.method == 'POST':
        try:
            audio_data = JSONParser().parse(request)
            if audioFileType.lower() == 'song':
                song_obj = Song.objects.filter(id=id).first()
                if song_obj:
                    song_obj.song_name = audio_data.get('song_name')
                    song_obj.duration = audio_data.get('duration')
                    song_obj.save()
                    return JsonResponse({'success':'updated'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'failed':'detail not found'}, status=status.HTTP_200_OK)
            elif audioFileType.lower() == 'podcast':
                podcast_obj = Podcast.objects.filter(id=id).first()
                if podcast_obj:
                    if len(audio_data.get('participants')) > 10 or type(audio_data.get('participants')) != list:
                        return JsonResponse({'error':"Participants more than 10 is not allowed or type mismatched"})
                    else:
                        podcast_obj.podcast_name = audio_data.get('podcast_name')
                        podcast_obj.host = audio_data.get('host')
                        podcast_obj.participants = audio_data.get('participants')
                        podcast_obj.duration = audio_data.get('duration')
                        podcast_obj.save()
                    return JsonResponse({'success':'updated'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'failed':'detail not found'}, status=status.HTTP_200_OK)        
            elif audioFileType.lower() == 'audiobook':
                audiobook_obj = Audiobook.objects.filter(id=id).first()
                if audiobook_obj:
                    audiobook_obj.audio_title = audio_data.get('audio_title')
                    audiobook_obj.author = audio_data.get('author')
                    audiobook_obj.narrator = audio_data.get('narrator')
                    audiobook_obj.duration = audio_data.get('duration')
                    audiobook_obj.save()
                    return JsonResponse({'success':'updated'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'failed':'detail not found'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'failed':'audioFileType missmatch'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error':str(e)})
    return JsonResponse({'done':'success'})



# ContactSerializer(query, many=True).data
@csrf_exempt
def listdetail(request, **kwargs):
    if request.method == 'GET':
        audioFileType = kwargs.get('audioFileType')
        id = kwargs.get('id')
        try:
            if audioFileType.lower() == 'song':
                if id:
                    song_obj = Song.objects.filter(id=id).first()
                    serializer = SongSerializer(song_obj)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
                else:
                    song_objs = Song.objects.all()
                    serializer = SongSerializer(song_objs, many=True)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            elif audioFileType.lower() == 'podcast':
                if id:
                    podcast_obj = Podcast.objects.filter(id=id).first()
                    serializer = PodcastSerializer(podcast_obj)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
                else:
                    podcast_obj = Podcast.objects.all()
                    serializer = PodcastSerializer(podcast_obj, many=True)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)    

            elif audioFileType.lower() == 'audiobook':
                if id:
                    audiobook_obj = Audiobook.objects.filter(id=id).first()
                    serializer = AudiobookSerializer(audiobook_obj)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
                else:
                    audiobook_obj = Audiobook.objects.all()
                    serializer = AudiobookSerializer(audiobook_obj, many=True)
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)     
            else:
                return JsonResponse({'failed':'audioFileType missmatch'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error':str(e)})
    return JsonResponse({'done':'success'})