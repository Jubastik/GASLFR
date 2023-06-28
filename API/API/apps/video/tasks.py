from time import sleep

from API.apps.video.models import Result
from API.settings.celery import app


@app.task(bind=True)
def process_video(self, video_id):
    print("start processing")
    sleep(10)
    print("end processing")
    Result.objects.create(video_id=video_id, timecodes={"test": "test"})