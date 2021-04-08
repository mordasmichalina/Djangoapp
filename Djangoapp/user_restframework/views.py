from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserRegisterViewSet(CreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
