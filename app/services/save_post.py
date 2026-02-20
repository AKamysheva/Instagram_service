from django.utils.dateparse import parse_datetime
from app.models import Post


def save_posts(posts: list[dict]) -> None:
    """
    Saving media posts from Instagram Graph API to the database.
    """
    for post in posts:
        Post.objects.update_or_create(
            instagram_media_id=post["id"],
            defaults={
                "media_type": post["media_type"],
                "media_url": post["media_url"],
                "permalink": post["permalink"],
                "timestamp": parse_datetime(post["timestamp"]),
            },
        )
