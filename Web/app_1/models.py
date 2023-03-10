from django.db import models


class UserQueryRequest(models.Model):
    query_text = models.CharField(max_length=1024)
    audio_wave_file = models.FileField(upload_to="audio_wave_files")
