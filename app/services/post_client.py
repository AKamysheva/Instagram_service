import requests
from instagram_service.config import settings
from app.services.save_post import save_posts


class InstagramPostsClient:
    """
    The client for getting user media via the Instagram Graph API.
    """

    INSTAGRAM_URL = "https://graph.instagram.com/v25.0"

    def __init__(self) -> None:
        self.token = settings.INSTAGRAM_USER_ACCESS_TOKEN
        self.user_id = settings.INSTAGRAM_USER_ID

    def get_media_from_user(self) -> None:
        url = f"{self.INSTAGRAM_URL}/{self.user_id}/media"
        params = {
            "fields": "id,media_type,media_url,permalink,timestamp",
            "access_token": self.token,
        }
        while url:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if data.get("data"):
                save_posts(data["data"])
            # pagination
            url = data.get("paging", {}).get("next")
            params = None
