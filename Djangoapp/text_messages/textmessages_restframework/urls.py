from django.conf.urls import url
from rest_framework import routers
from django.urls import include, path

from .views import (
    MessageListAPIView,
    MessageCreateAPIView,
)


urlpatterns = [
    url(r'^$', MessageListAPIView.as_view(), name='list'),
    url(r'^create/$', MessageCreateAPIView.as_view(), name='create'),
]