from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image


def filename(instance):
    now = timezone.now()
    return str(str(now)+'.jpg')


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    destination = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.FileField(upload_to=filename, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


