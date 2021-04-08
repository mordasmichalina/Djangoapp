
from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import Message


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id',
            'name',
            'email',
            'message',
        ]
