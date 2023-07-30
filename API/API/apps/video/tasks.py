import logging
from time import sleep

from API.apps.video.models import Result, Video
from API.settings.celery import app, ml_client


@app.task(bind=True)
def process_video(self, video_id):
    video = Video.objects.get(pk=video_id)
    video_path = video.clip.path
    job = ml_client.submit(video_path)
    while job.status().success is None:
        sleep(3)
        video.status = job.status().code
        video.save()
    if job.status().success:
        Result.objects.create(video_id=video_id, timecodes={"test": job.result()})
    else:
        logging.error(job.result())
