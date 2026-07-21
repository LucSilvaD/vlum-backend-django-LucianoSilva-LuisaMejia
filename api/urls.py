from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'directors', views.DirectorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

