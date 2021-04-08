from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name