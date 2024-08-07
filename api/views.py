from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album,Artist,Song
from . serializers import ArtistSerializer,ArtistSerializerMobile,AlbumSerializer,SongSerializer

class ArtistAPIView(APIView):
    def get_queryset(self):
        return Artist.objects.all()
    def get(self, request):
        query=self.get_queryset()
        search_data=request.query_params.get("search")
        if search_data is  not None:
            query=query.filter(username__icontains=search_data) | query.filter(first_name__icontains=search_data)| query.filter(last_name__icontains=search_data)
        serializer = ArtistSerializer(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "message": "Error"
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)



class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "message": "Error"
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artists, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artists, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artists = Artist.objects.get(id=id)
        artists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ArtistAPIMobileView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializerMobile(queryset, many=True)
        return Response(data=serializer.data)




class AlbumAPIView(APIView):
    def get_queryset(self):
        return Album.objects.all()
    def get(self, request):
        query=self.get_queryset()
        search_data=request.query_params.get("search")
        if search_data is not None:
            query=query.filter(title__icontains=search_data)
        album_serializer = AlbumSerializer(query, many=True)
        return Response(data=album_serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "message": "Error"
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetailAPIView(APIView):
    def get(self, request, id):
        albums = Album.objects.get(id=id)
        serializer = AlbumSerializer(albums)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        albums = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=albums, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        albums = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=albums, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albums = Album.objects.get(id=id)
        albums.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongAPIView(APIView):
    def get_queryset(self):
        return Song.objects.all()
    def get(self, request):
        query=self.get_queryset()
        search_data=request.query_params.get("search")
        if search_data is not None:
            query=query.filter(title__icontains=search_data) | query.filter(album__artist__first_name__icontains=search_data) | query.filter(album__artist__last_name__icontains=search_data)

        serializer = SongSerializer(query, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error={
            "status":400,
            "message":"Error"
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)





class SongDetailAPIView(APIView):
    def get(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(song)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






