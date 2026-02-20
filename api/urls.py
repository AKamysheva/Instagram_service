from django.urls import path
from .views import CreateCommentView, PostListView, SyncView


urlpatterns = [
    path("sync/", SyncView.as_view(), name="sync"),
    path("posts/", PostListView.as_view(), name="posts"),
    path(
        "posts/<int:id>/comment/",
        CreateCommentView.as_view(),
        name="comments",
    ),
]
