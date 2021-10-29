import os
import sys

from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"listings/{instance.object_id}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class Post(models.Model):
    object_id = models.CharField(max_length=11, null=False, blank=False)
    image1 = models.ImageField(null=False, blank=False, upload_to=upload_to)
    image2 = models.ImageField(null=True, blank=True, upload_to=upload_to)
    image3 = models.ImageField(null=True, blank=True, upload_to=upload_to)
    image4 = models.ImageField(null=True, blank=True, upload_to=upload_to)
    image5 = models.ImageField(null=True, blank=True, upload_to=upload_to)
    image6 = models.ImageField(null=True, blank=True, upload_to=upload_to)
    description = models.TextField(null=True, blank=True)
    headline = models.CharField(max_length=140, null=False, blank=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.object_id
