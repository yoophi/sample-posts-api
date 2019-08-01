from unittest import mock

import pytest

from app.domain.post import Post
from app.request_objects.post import PostItemRequestObject
from app.use_cases import PostItemUseCase


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


def test_post_item_with_params(domain_posts):
    repo = mock.Mock()
    repo.post_item.return_value = domain_posts[0]

    post_item_use_case = PostItemUseCase(repo)
    request = PostItemRequestObject(id=1)

    response = post_item_use_case.execute(request)

    assert bool(response) is True
    repo.post_item.assert_called_with(1)
    assert response.value == domain_posts[0]
