from rest_framework import serializers

from API.apps.video.models import Video


class VideoSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.CharField( read_only=True)
    timecodes = serializers.JSONField(read_only=True, source="result.timecodes")

    class Meta:
        model = Video
        fields = '__all__'
