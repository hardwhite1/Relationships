from rest_framework import serializers

from .models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'email', 'phone', 'id']


class AlbumSerializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'id', 'artists']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'duration', 'album', 'id']


class ArtistAlbumSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Artist
        fields = ['name', 'phone', 'albums']
