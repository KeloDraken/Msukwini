from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from msukwini.core.posts.models import Post
from msukwini.core.posts.serialisers import PostListSerialiser


class PostListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all().order_by("-datetime_created")
        serialiser = PostListSerialiser(
            queryset, many=True, context={"request": request}
        )
        return Response(data=serialiser.data, status=status.HTTP_200_OK)


post_list_view = PostListAPIView.as_view()
