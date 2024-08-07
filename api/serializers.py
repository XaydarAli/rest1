from rest_framework import serializers
from .models import Album,Artist,Song



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name','last_name','username')


class ArtistSerializerMobile(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name','last_name')




class AlbumSerializer(serializers.ModelSerializer):
    artist=ArtistSerializerMobile()
    class Meta:
        model = Album
        fields = ('id','title','artist')




class SongSerializer(serializers.ModelSerializer):
    album=AlbumSerializer()
    class Meta:
        model = Song
        fields = ('id','title','album')
