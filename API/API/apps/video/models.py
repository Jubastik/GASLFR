from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    class Status(models.TextChoices):
        STARTING = "STARTING"
        JOINING_QUEUE = "JOINING_QUEUE"
        QUEUE_FULL = "QUEUE_FULL"
        IN_QUEUE = "IN_QUEUE"
        SENDING_DATA = "SENDING_DATA"
        PROCESSING = "PROCESSING"
        ITERATING = "ITERATING"
        PROGRESS = "PROGRESS"
        FINISHED = "FINISHED"
        CANCELLED = "CANCELLED"

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.FileField(upload_to='clips/')
    upload = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.STARTING)

    @classmethod
    def get_path(cls, video_id: int):
        return cls.objects.get(pk=video_id).clip

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['-upload']


class Result(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    timecodes = models.JSONField()

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
