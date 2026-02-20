import requests
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound
from app.models import Post, Comment
from app.services.post_client import InstagramPostsClient
from app.services.comment_client import InstagramCommentsClient
from .serializers import PostSerializer, CommentSerializer
from .pagination import PostCursorPagination


def api_root(response):
    return JsonResponse(
        {
            "project": "Instagran Service",
            "endpoints": {
                "sync": "/api/sync/",
                "posts": "api/posts/",
                "create-comment": "api/posts/<int:instagram_media_id>/comment/",
            },
        }
    )


class SyncView(APIView):
    def post(self, request):
        client = InstagramPostsClient()
        client.get_media_from_user()
        return Response({"status": "sync completed"})


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostCursorPagination


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs["id"]

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        text = serializer.validated_data["text"]

        client = InstagramCommentsClient()
        try:
            response = client.create_comment(post.instagram_media_id, text)
        except requests.RequestException as e:
            raise APIException(f"Instagram API error: {e}")

        serializer.save(
            post=post,
            instagram_comment_id=response.get("id"),
        )
