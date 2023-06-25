from django.contrib.auth.models import User
from django.db import models
from time import sleep

from API.settings.celery import app


# Create your models here.
class Video(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.FileField(upload_to='clips/')
    upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['-upload']


class Result(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    error_code = models.IntegerField(default=0)
    timecodes = models.JSONField()

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    @classmethod
    @app.task(bind=True)
    def start_processing(cls, self, video_id) -> None:
        print("start processing")
        sleep(1)
        print("end processing")
        cls.objects.create(video_id=video_id, timecodes={"test": "test"})



