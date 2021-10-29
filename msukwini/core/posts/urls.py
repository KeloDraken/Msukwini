from django.urls import path

from msukwini.core.posts.views import post_list_view

app_name = "posts"

urlpatterns = [
    path("latest/", post_list_view, name="post-list-view"),
]
