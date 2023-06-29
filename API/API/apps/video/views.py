from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from API.apps.video.models import Video
from API.apps.video.serializers import VideoSerializer
from API.permissions import IsOwner
from .tasks import process_video


class VideoAPIList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        process_video.delay(res.data['id'])
        return res


class VideoAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsOwner,)
