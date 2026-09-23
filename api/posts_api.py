"""Reusable client for JSONPlaceholder Posts API."""
import requests

class PostsAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, timeout=10):
        self.timeout = timeout

    def get_posts(self):
        return requests.get(f"{self.BASE_URL}/posts", timeout=self.timeout)

    def get_post(self, post_id):
        return requests.get(f"{self.BASE_URL}/posts/{post_id}", timeout=self.timeout)
