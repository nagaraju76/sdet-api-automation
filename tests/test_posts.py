from utils.constants import (
    EXPECTED_POST_COUNT,
    EXPECTED_POST_FIELDS,
    VALID_POST_ID,
)


class TestPostsAPI:

    def test_get_posts_returns_successful_response(self, posts_api):
        response = posts_api.get_posts()

        assert response.status_code == 200
        assert response.headers.get("Content-Type", "").startswith(
            "application/json"
        )

    def test_get_posts_returns_expected_collection(self, posts_api):
        response = posts_api.get_posts()
        posts = response.json()

        assert isinstance(posts, list)
        assert len(posts) == EXPECTED_POST_COUNT

    def test_each_post_contains_expected_fields_and_types(self, posts_api):
        posts = posts_api.get_posts().json()

        for post in posts:
            assert EXPECTED_POST_FIELDS.issubset(post.keys())

            assert isinstance(post["userId"], int)
            assert isinstance(post["id"], int)
            assert isinstance(post["title"], str)
            assert isinstance(post["body"], str)

            assert post["id"] > 0
            assert post["userId"] > 0

    def test_get_post_by_valid_id(self, posts_api):
        response = posts_api.get_post(VALID_POST_ID)

        assert response.status_code == 200

        post = response.json()

        assert EXPECTED_POST_FIELDS.issubset(post.keys())
        assert post["id"] == VALID_POST_ID