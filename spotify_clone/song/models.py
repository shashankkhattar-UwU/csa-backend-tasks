from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Track(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    image=models.ImageField(upload_to='music_pics', default='default_spotify.png')
    audio=models.FileField(upload_to='music_file', default='default_song.mp3')
    views=models.IntegerField(default=0)
    likes=models.ManyToManyField(User, related_name='spotify_tracks')
    date_uploaded=models.DateTimeField(default=timezone.now)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def total_likes(self):
    #     return self.likes.count()
    
    def newView(self):
        self.views += 1
        self.save()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("track-detail", kwargs={"pk": self.pk})
    