##  A service that synchronizes content from Instagram to a local database and allows you to manage comments via API.

## Особенности
- API-эндпоинты:
   - ```POST /api/sync/``` —  download all user media objects from the Instagram Graph API and save to database;
   - ```GET /api/posts/``` — get a list of all saved posts from the local database;
   - ```POST /api/posts/{id}/comment/``` — send the comment text to the Instagram API for the post and save the comment to the local database

## Stack
- Backend: Python, Django, Django REST Framework
- Database: PostgreSQL
- Dependency manager: Poetry
- Containerization: Docker, Docker Compose

## Installation
1. Clone the repository:
   ```
   https://github.com/AKamysheva/Instagram_service.git
   ```

2. Create an .env file in the root (example below)
3. Install dependencies
   ```
   poetry install
   ```
4. Build and start the Containers:
   ```
   docker-compose up --build -d
   ```
.env File Example
```
SECRET_KEY=djando_secret_key
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
DEBUG=False
INSTAGRAM_USER_ACCESS_TOKEN=mytoken
INSTAGRAM_USER_ID=myuserid
```
You can generate an Instagram token at [Meta for Developers](https://developers.facebook.com/).

API доступен по адресу — ```http://localhost:8300/```

