import pytest

from app.domain.comment import Comment
from app.domain.post import Post
from app.repository import MemRepo


@pytest.fixture
def data_dicts():
    return {
        "posts": [
            {"id": 1, "title": "title one", "body": "body one"},
            {"id": 2, "title": "title two", "body": "body two"},
            {"id": 3, "title": "title three", "body": "body three"},
            {"id": 4, "title": "title four", "body": "body four"},
            {"id": 5, "title": "title five", "body": "body five"},
            {"id": 6, "title": "title six", "body": "body six"},
        ],
        "comments": [
            {"id": 1, "post_id": 1, "body": "comment body one"}
        ]
    }


def test_repository_post_list_without_parameters(data_dicts):
    repo = MemRepo(data_dicts)
    posts = [Post.from_dict(d) for d in data_dicts["posts"]]

    assert repo.post_list() == posts


def test_repository_post_item(data_dicts):
    repo = MemRepo(data_dicts)
    posts = [Post.from_dict(d) for d in data_dicts["posts"] if d["id"] == 1]
    posts_1 = posts[0]
    posts_1.comments = [Comment.from_dict(d) for d in data_dicts["comments"] if d["post_id"] == 1]

    resp = repo.post_item(1)
    assert resp == posts_1


def test_repository_post_item_with_invalid_id(data_dicts):
    repo = MemRepo(data_dicts)

    assert repo.post_item(999) is None


def test_repository_post_create_with_valid_dict():
    repo = MemRepo({})

    post1 = repo.post_create({"title": "title one", "body": "body one"})
    assert isinstance(post1, Post)
    assert post1.id == 1
    assert post1.title == "title one"
    assert post1.body == "body one"

    post2 = repo.post_create({"title": "title two", "body": "body two"})
    assert post2.id == 2


def test_repository_comment_create_with_valid_dict():
    repo = MemRepo({})

    comment1 = repo.comment_create({"post_id": 1, "body": "body one"})
    assert isinstance(comment1, Comment)
    assert comment1.id == 1
    assert comment1.post_id == 1
    assert comment1.body == "body one"
