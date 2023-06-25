from rest_framework import serializers

from API.apps.video.models import Video, Result


class VideoSerializer(serializers.ModelSerializer):
    error_code = serializers.IntegerField(read_only=True, source="result.error_code")
    timecodes = serializers.JSONField(read_only=True, source="result.timecodes")

    class Meta:
        model = Video
        fields = '__all__'
