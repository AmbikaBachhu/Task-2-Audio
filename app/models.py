from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.FloatField()
    audio_file = models.FileField(upload_to='upload/audiofiles', blank=True, )

    def __str__(self):
        return self.title
