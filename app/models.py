from django.db import models


class Post(models.Model):
    instagram_media_id = models.BigIntegerField(unique=True, verbose_name="Post`s ID")
    media_type = models.CharField(max_length=50, verbose_name="Type of content")
    media_url = models.URLField(max_length=1000, verbose_name="Media URL")
    permalink = models.URLField(verbose_name="URL Post")
    timestamp = models.DateTimeField(verbose_name="Date of publication")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    instagram_comment_id = models.CharField(
        max_length=100, unique=True, null=True, blank=True
    )
    text = models.TextField(verbose_name="Comment on the post")
    timestamp = models.DateTimeField(auto_now_add=True)
