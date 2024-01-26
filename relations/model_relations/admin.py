from django.contrib import admin
from model_relations.models import Artist, Album, Song


# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    list_per_page = 25


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year']
    list_per_page = 25


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'album']
    list_per_page = 25
