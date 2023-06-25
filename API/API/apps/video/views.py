from rest_framework import generics

from API.apps.video.models import Video, Result
from API.apps.video.serializers import VideoSerializer


class VideoAPIList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        Result.start_processing(res.data["id"])
        return res


class VideoAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
