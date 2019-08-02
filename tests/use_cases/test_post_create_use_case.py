from unittest import mock

import pytest

from app.core.domain.post import Post
from app.core.request_objects.post import PostCreateRequestObject
from app.core.use_cases import PostCreateUseCase


@pytest.fixture
def domain_posts():
    posts = [{"id": 1, "title": "title one", "body": "body one"}]

    return [Post.from_dict(post) for post in posts]


def test_post_create_with_valid_data(domain_posts):
    repo = mock.Mock()
    repo.post_create.return_value = domain_posts[0]

    post_create_use_case = PostCreateUseCase(repo)
    request = PostCreateRequestObject.from_dict(
        {"title": "title one", "body": "body one"}
    )
    response = post_create_use_case.execute(request)

    assert bool(response) is True
    repo.post_create.assert_called_with({"title": "title one", "body": "body one"})
    assert response.value == domain_posts[0]
