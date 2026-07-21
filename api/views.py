from rest_framework import viewsets
from vlum.models import Movie, Director
from .serializers import MovieSerializer, DirectorSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        return [AllowAny()]

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        return [AllowAny()]

