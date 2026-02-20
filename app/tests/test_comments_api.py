from requests import RequestException
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from app.models import Post, Comment


class CommentAPITest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(
            instagram_media_id="123456",
            media_type="IMAGE",
            media_url="https://example.com/test",
            permalink="https://instagram.com/p/test/",
            timestamp="2025-09-01T00:00:00+0000",
        )
        self.data = {"text": "Test comment"}

    @patch("api.views.InstagramCommentsClient.create_comment")
    def test_create_comment_success(self, mock_create_comment):
        mock_create_comment.return_value = {"id": "111"}
        url = reverse("comments", kwargs={"id": self.post.pk})

        response = self.client.post(url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

        comment = Comment.objects.first()

        self.assertEqual(comment.text, "Test comment")
        self.assertEqual(comment.instagram_comment_id, "111")

        self.assertEqual(response.data["instagram_comment_id"], "111")
        self.assertEqual(response.data["text"], "Test comment")

    @patch("api.views.InstagramCommentsClient.create_comment")
    def test_create_comment_with_error(self, mock_create_comment):
        mock_create_comment.side_effect = RequestException("Instagram failure")

        url = reverse(
            "comments",
            kwargs={"id": self.post.pk},
        )

        response = self.client.post(url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(Comment.objects.count(), 0)
