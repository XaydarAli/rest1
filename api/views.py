from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Album,Artist,Song
from . serializers import ArtistSerializer,AlbumSerializer,SongSerializer
from . serializers import ArtistMobileSerializer,AlbumMobileSerializer,SongMobileSerializer
from .serializers import ArtisttelebotSerializer,AlbumtelebotSerializer,SongtelebotSerializer

# class ArtistAPIView(APIView):
#     def get_queryset(self):
#         return Artist.objects.all()
#     def get(self, request):
#         query=self.get_queryset()
#         search_data=request.query_params.get("search")
#         if search_data is  not None:
#             query=query.filter(username__icontains=search_data) | query.filter(first_name__icontains=search_data)| query.filter(last_name__icontains=search_data)
#         serializer = ArtistSerializer(query, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ArtistSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         context_error = {
#             "status": 400,
#             "message": "Error"
#         }
#
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class ArtistDetailAPIView(APIView):
#     def get(self, request, id):
#         artist = Artist.objects.get(id=id)
#         serializer = ArtistSerializer(artist)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
#     def post(self, request):
#         serializer = ArtistSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         context_error = {
#             "status": 400,
#             "message": "Error"
#         }
#
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def put(self, request, id):
#         artists = Artist.objects.get(id=id)
#         serializer = ArtistSerializer(instance=artists, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         artists = Artist.objects.get(id=id)
#         serializer = ArtistSerializer(instance=artists, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         artists = Artist.objects.get(id=id)
#         artists.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
# class ArtistAPIMobileView(APIView):
#     def get(self, request):
#         queryset = Artist.objects.all()
#         serializer = ArtistSerializerMobile(queryset, many=True)
#         return Response(data=serializer.data)
class ArtistAPIViewSET(ModelViewSet):
    queryset = Artist.objects.filter(status='pb')
    serializer_class = ArtistSerializer
    permission_classes = (IsAuthenticated,)


    # serializer_class = ArtistSerializer
    # def get_queryset(self):
    #     return Artist.objects.all()


    @action(detail=True, methods=['GET', ])
    def num_of_listen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.profile_views += 1
        artist.save()
        return Response(data={"Profile Viewed": artist.profile_views})

    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        artists = self.get_queryset().order_by('-profile_views')[:3]
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def not_viewed(self, request, *args, **kwargs):
        artists = self.get_queryset().filter(num_of_listens=0)
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def all_viewed_artists(self, request, *args, **kwargs):
        artists = self.get_queryset()
        for artist in artists:
            artist.profile_views += 1
            artist.save()
        return Response(data={"message": "All Artists' profiles are viewed "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_draft(self, request, *args, **kwargs):
        artists = self.get_queryset()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "Not allowed to see profiles "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "Access given to see profiles "}, status=status.HTTP_200_OK)


#

class AlbumAPIViewSET(ModelViewSet):
    queryset = Album.objects.filter(status='pb')
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET', ])
    def num_of_listen(self, request, *args, **kwargs):
        album = self.get_object()
        album.num_of_listens += 1
        album.save()
        return Response(data={"listened": album.num_of_listens})



    @action(detail=False, methods=['GET',])
    def top(self,request,*args,**kwargs):
        albums=self.get_queryset().order_by('-num_of_listens')[:3]
        serializer=AlbumSerializer(albums,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def not_listened(self,request,*args,**kwargs):
        albums=self.get_queryset().filter(num_of_listens=0)
        serializer=AlbumSerializer(albums,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def all_listened_albums(self, request, *args, **kwargs):
        albums = self.get_queryset()
        for album in albums:
            album.num_of_listens += 1
            album.save()
        return Response(data={"message":"All albums are listened "} )

    @action(detail=False, methods=['GET', ])
    def to_draft(self, request, *args, **kwargs):
        albums = self.get_queryset()
        for album in albums:
            album.pb_to_df()
        return Response(data={"message": "All albums  are drafted "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        albums = Album.objects.all()
        for album in albums:
            album.df_to_pb()
        return Response(data={"message": "All albums  are published "}, status=status.HTTP_200_OK)


#
# class AlbumAPIView(APIView):
#     def get_queryset(self):
#         return Album.objects.all()
#     def get(self, request):
#         query=self.get_queryset()
#         search_data=request.query_params.get("search")
#         if search_data is not None:
#             query=query.filter(title__icontains=search_data)
#         album_serializer = AlbumSerializer(query, many=True)
#         return Response(data=album_serializer.data)
#
#     def post(self, request):
#         serializer = AlbumSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         context_error = {
#             "status": 400,
#             "message": "Error"
#         }
#
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
# class AlbumDetailAPIView(APIView):
#     def get(self, request, id):
#         albums = Album.objects.get(id=id)
#         serializer = AlbumSerializer(albums)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, id):
#         albums = Album.objects.get(id=id)
#         serializer = AlbumSerializer(instance=albums, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         albums = Album.objects.get(id=id)
#         serializer = AlbumSerializer(instance=albums, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         albums = Album.objects.get(id=id)
#         albums.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class SongAPIViewSET(ModelViewSet):
    queryset = Song.objects.filter(status='pb')
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET',])
    def num_of_listen(self,request,*args,**kwargs):
        song=self.get_object()
        song.num_of_listens+=1
        song.save()
        return Response(data={"listened":song.num_of_listens})

    @action(detail=False, methods=['GET',])
    def top(self,request,*args,**kwargs):
        songs=self.get_queryset().order_by('-num_of_listens')[:3]
        serializer=SongSerializer(songs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def not_listened(self,request,*args,**kwargs):
        songs=self.get_queryset().filter(num_of_listens=0)
        serializer=SongSerializer(songs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def all_listened_songs(self, request, *args, **kwargs):
        songs = self.get_queryset()
        for song in songs:

            song.num_of_listens += 1
            song.save()
        return Response(data={"message":"All musics are listened "}, status=status.HTTP_200_OK )


    @action(detail=False, methods=['GET', ])
    def to_draft(self,request,*args,**kwargs):
        songs=self.get_queryset()
        for song in songs:
            song.pb_to_df()
        return Response(data={"message":"All musics  are drafted "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        songs = Song.objects.all()
        for song in songs:
            song.df_to_pb()
        return Response(data={"message": "All musics  are published "}, status=status.HTTP_200_OK)



#
# class SongAPIView(APIView):
#     def get_queryset(self):
#         return Song.objects.all()
#     def get(self, request):
#         query=self.get_queryset()
#         search_data=request.query_params.get("search")
#         if search_data is not None:
#             query=query.filter(title__icontains=search_data) | query.filter(album__artist__first_name__icontains=search_data) | query.filter(album__artist__last_name__icontains=search_data)
#
#         serializer = SongSerializer(query, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         context_error={
#             "status":400,
#             "message":"Error"
#         }
#
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#
# class SongDetailAPIView(APIView):
#     def get(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(song)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#
#     def put(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#     def delete(self, request, id):
#         song = Song.objects.get(id=id)
#         song.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
#


class ArtistMobileAPIViewSET(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistMobileSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

class AlbumMobileAPIViewSET(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumMobileSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)


class SongMobileAPIViewSET(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongMobileSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)






class ArtisttelebotAPIViewSET(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtisttelebotSerializer

class AlbumtelebotAPIViewSET(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumtelebotSerializer


class SongtelebotAPIViewSET(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongtelebotSerializer

