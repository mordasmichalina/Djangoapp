from ..models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from .serializers import PostSerializer, PostCreateSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
