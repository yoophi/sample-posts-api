from unittest import mock

import pytest

from app.domain.comment import Comment
from app.request_objects.comment import CommentCreateRequestObject
from app.use_cases import CommentCreateUseCase


@pytest.fixture
def domain_comments():
    comments = [{"post_id": 1, "body": "body one"}]

    return [Comment.from_dict(post) for post in comments]


def test_comment_create_with_valid_data(domain_comments):
    repo = mock.Mock()
    repo.comment_create.return_value = domain_comments[0]

    comment_create_use_case = CommentCreateUseCase(repo)
    request = CommentCreateRequestObject.from_dict(
        {"post_id": 1, "body": "body one"}
    )
    response = comment_create_use_case.execute(request)

    assert bool(response) is True
    repo.comment_create.assert_called_with({"post_id": 1, "body": "body one"})
    assert response.value == domain_comments[0]
