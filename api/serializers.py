from rest_framework import serializers
from .models import Album,Artist,Song



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','first_name','last_name','profile_views','status')







class AlbumSerializer(serializers.ModelSerializer):
    #artist=ArtistSerializer()
    class Meta:
        model = Album
        fields = ('id','title','num_of_listens','status')




class SongSerializer(serializers.ModelSerializer):
    #album=AlbumSerializer()
    class Meta:
        model = Song
        fields = ('id','title','num_of_listens','status')









class ArtistMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name','last_name')




class AlbumMobileSerializer(serializers.ModelSerializer):
    artist=ArtistMobileSerializer()
    class Meta:
        model = Album
        fields = ('title','artist')


class SongMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title','album')












class ArtisttelebotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('username','first_name','last_name')




class AlbumtelebotSerializer(serializers.ModelSerializer):
    artist=ArtistMobileSerializer()
    class Meta:
        model = Album
        fields = ('title','artist')


class SongtelebotSerializer(serializers.ModelSerializer):
    album = AlbumtelebotSerializer()

    class Meta:
        model = Song
        fields = ('title','album')