from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album,Artist,Song
from . serializers import ArtistSerializer,ArtistSerializerMobile,AlbumSerializer,SongSerializer

class ArtistAPIView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data)




class ArtistAPIMobileView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializerMobile(queryset, many=True)
        return Response(data=serializer.data)




class AlbumAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        album_serializer = AlbumSerializer(albums, many=True)
        return Response(data=album_serializer.data)



class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        song_serializer = SongSerializer(songs, many=True)
        return Response(data=song_serializer.data)