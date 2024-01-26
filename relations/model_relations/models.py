from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    title = models.CharField(max_length=155)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist, related_name='albums')  # this line here creates a many-to-many relationship between Album and
    # Artist

    def __str__(self):
        return f"Album: {self.title} ,{self.release_year}"

class Song(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return f"{self.name}"