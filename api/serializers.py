from rest_framework import serializers
from vlum.models import Movie, Director
from django.core.files.base import ContentFile
import base64

class MovieSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'movie.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value

class DirectorSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Director
        fields = '__all__'

    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'director.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value
