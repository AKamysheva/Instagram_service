from rest_framework import pagination


class PostCursorPagination(pagination.CursorPagination):
    page_size = 5
    ordering = "-timestamp"
