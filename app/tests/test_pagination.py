from unittest.mock import patch, MagicMock
from django.test import TestCase
from app.services.post_client import InstagramPostsClient


class InstagramPostsClientTests(TestCase):

    @patch("app.services.post_client.save_posts")
    @patch("app.services.post_client.requests.get")
    def test_get_media_from_user_pagination(self, mock_get, mock_save_posts):
        first_page = {
            "data": [
                {
                    "id": "1",
                    "media_type": "IMAGE",
                    "media_url": "url1",
                    "permalink": "p1",
                    "timestamp": "2026-01-01T00:00:00+0000",
                },
                {
                    "id": "2",
                    "media_type": "IMAGE",
                    "media_url": "url2",
                    "permalink": "p2",
                    "timestamp": "2026-01-02T00:00:00+0000",
                },
            ],
            "paging": {"next": "https://graph.instagram.com/next_page"},
        }

        second_page = {
            "data": [
                {
                    "id": "3",
                    "media_type": "IMAGE",
                    "media_url": "url3",
                    "permalink": "p3",
                    "timestamp": "2026-01-03T00:00:00+0000",
                },
            ],
            "paging": {},
        }

        # настройка моков для requests.get
        mock_get.side_effect = [
            MagicMock(status_code=200, json=MagicMock(return_value=first_page)),
            MagicMock(status_code=200, json=MagicMock(return_value=second_page)),
        ]

        client = InstagramPostsClient()
        client.get_media_from_user()

        self.assertEqual(mock_get.call_count, 2)

        self.assertEqual(mock_save_posts.call_count, 2)

        mock_save_posts.assert_any_call(first_page["data"])
        mock_save_posts.assert_any_call(second_page["data"])
