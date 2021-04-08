from ..models import Message
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from .serializers import MessageSerializer

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = (BasicAuthentication,)