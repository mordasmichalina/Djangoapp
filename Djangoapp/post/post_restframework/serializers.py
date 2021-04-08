
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from rest_framework import serializers
from ..models import Post, PostImage
from rest_framework.filters import SearchFilter, OrderingFilter


class PostImageSerializer(ModelSerializer):
    image = SerializerMethodField('get_image')

    class Meta:
        model = PostImage
        fields = [
            'image'
        ]
        read_only_fields = ['post']

    def get_image(self, instance):
        try:
            request = self.context.get("request")
            image = request.build_absolute_uri(instance.image.url)
        except:
            image = None
        return image


class PostSerializer(ModelSerializer):
    images = PostImageSerializer(source='postimage_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'timestamp',
            'price',
            'duration',
            'destination',
            'images'
        ]


class PostCreateSerializer(ModelSerializer):

    title = serializers.CharField(default='')
    content = serializers.CharField(default='')
    price = serializers.CharField(default=0.0)
    duration = serializers.DurationField(default=0)
    destination = serializers.CharField(default='')
    images = serializers.ListField(child=serializers.ImageField(), default='')

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'price',
            'duration',
            'destination',
            'images',
        ]

    def create(self, validated_data):
        title = validated_data['title']
        content = validated_data['content']
        price = validated_data['price']
        duration = validated_data['duration']
        destination = validated_data['destination']
        images = validated_data['images']

        post_obj = Post.objects.create(
            title=title,
            content=content,
            price=price,
            duration=duration,
            destination=destination,
        )

        PostImage.objects.bulk_create([PostImage(post=post_obj, image=i) for i in images])
        return validated_data


class PostUpdateSerializer(ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    duration = serializers.DurationField(required=False)
    destination = serializers.CharField(required=False)
    images = serializers.ListField(child=serializers.ImageField(), required=False)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'price',
            'duration',
            'destination',
            'images',
        ]

    def create(self, validated_data):
        title = validated_data['title']
        content = validated_data['content']
        price = validated_data['price']
        duration = validated_data['duration']
        destination = validated_data['destination']
        images = validated_data['images']

        post_obj = Post.objects.update(
            title=title,
            content=content,
            price=price,
            duration=duration,
            destination=destination,
        )

        PostImage.objects.bulk_update([PostImage(post=post_obj, image=i) for i in images])
        return validated_data