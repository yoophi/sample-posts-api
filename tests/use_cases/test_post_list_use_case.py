from unittest import mock

import pytest

from app.domain.post import Post
from app.request_objects.post import PostListRequestObject
from app.use_cases import PostListUseCase


@pytest.fixture
def domain_posts():
    posts = [
        {"id": 1, "title": "title one", "body": "body one"},
        {"id": 2, "title": "title two", "body": "body two"},
        {"id": 3, "title": "title three", "body": "body three"},
        {"id": 4, "title": "title four", "body": "body four"},
        {"id": 5, "title": "title five", "body": "body five"},
        {"id": 6, "title": "title six", "body": "body six"},
    ]

    return [Post.from_dict(post) for post in posts]


def test_post_list_without_params(domain_posts):
    repo = mock.Mock()
    repo.post_list.return_value = domain_posts

    post_list_use_case = PostListUseCase(repo)
    request = PostListRequestObject()

    response = post_list_use_case.execute(request)

    assert bool(response) is True
    repo.post_list.assert_called_with()
    assert response.value == domain_posts
