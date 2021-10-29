from rest_framework import serializers
from msukwini.core.posts.models import Post


class PostListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "object_id",
            "image1",
            "image2",
            "image3",
            "image4",
            "image5",
            "image6",
            "headline",
            "description",
            "datetime_created",
            "date_create",
        )
