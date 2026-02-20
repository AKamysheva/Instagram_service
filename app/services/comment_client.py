import requests
from instagram_service.config import settings


class InstagramCommentsClient:
    """
    A client for publishing comments via the Instagram Graph API.
    """

    INSTAGRAM_URL = "https://graph.instagram.com/v25.0"

    def __init__(self) -> None:
        self.token = settings.INSTAGRAM_USER_ACCESS_TOKEN

    def create_comment(self, post_id: int, text: str) -> dict:
        url = f"{self.INSTAGRAM_URL}/{post_id}/comments"
        params = {
            "message": text,
            "access_token": self.token,
        }
        response = requests.post(
            url,
            data=params,
        )
        response.raise_for_status()
        return response.json()
