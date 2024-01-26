from django.shortcuts import render
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song, Artist
from django.http import HttpResponse

from .serializers import ArtistSerializer, ArtistAlbumSerializer
from django.contrib import messages

#from relations.model_relations.serializers import ArtistAlbumSerializer


# Create your views here.
# def mine(request):
# mydata = Album.objects.all().values()
# template = loader.get_template("test.html")
# context = {
#    'mydata': mydata,
# }
# return HttpResponse(template.render(context, request))
def show(request):
    # artist = Artist.objects.order_by("?").first()
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #  print(alb.title, alb.release_year)
    # songs = alb.songs.all()
    # print(len(songs), "Songs")
    # for s in songs:
    #   print("songs are: ", s.name, -s.duration)
    song = Song.objects.order_by("?").first()
    album = song.album
    artist = album.artists.all().values("name")
    print(artist)
    print(album)
    print(song)
    return HttpResponse(artist)


@api_view(["GET", "POST"])
def save_or_fetch_artists(request):
    if request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistAlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Added artist", "data": serializer.data})

    return None


@api_view(["GET"])
def fetch_one_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)
@api_view(["DELETE"])
def delete_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        artist.delete()
        return Response({"message": "Successfully deleted"})
    except:
        return Response({"error": "Artist not found"}, status=404)

    return None

@api_view(["PUT", "PATCH"])
def update_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({"error": "Invalid Data"}, status=404)

    return None

@api_view(["GET"])
def albums_for_artist(request, id):
        try:
            artist = Artist.objects.get(pk=id)
            serializer = ArtistAlbumSerializer(instance=artist)
            return Response(serializer.data)
        except:
            return Response({"error": "Invalid Data"}, status=404)

