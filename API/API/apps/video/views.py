from rest_framework import generics

from API.apps.video.models import Video, Result
from API.apps.video.serializers import VideoSerializer
from .tasks import process_video


class VideoAPIList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        process_video.delay(res.data['id'])
        return res


class VideoAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
