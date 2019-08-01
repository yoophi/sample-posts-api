from app.domain.comment import Comment
from app.domain.post import Post


def test_post_model_init():
    id_ = 1
    post = Post(id=id_, title="title", body="body")
    assert post.id == id_
    assert post.title == "title"
    assert post.body == "body"
    assert post.comments == []


def test_post_model_init_with_comments():
    id_ = 1
    post = Post(
        id=id_, title="title", body="body", comments=[{"id": 1, "body": "comment body"}]
    )

    assert post.id == id_
    assert post.title == "title"
    assert post.body == "body"
    assert len(post.comments) == 1
    assert isinstance(post.comments[0], Comment)


def test_post_model_from_dict():
    post = Post.from_dict({"id": 1, "title": "title", "body": "body"})

    assert post.id == 1
    assert post.title == "title"
    assert post.body == "body"


def test_post_model_to_dict():
    post_dict = {"id": 1, "title": "title", "body": "body", "comments": []}

    post = Post.from_dict(post_dict)
    assert post.to_dict() == post_dict


def test_post_model_comparison():
    post_dict = {"id": 1, "title": "title", "body": "body"}

    post1 = Post.from_dict(post_dict)
    post2 = Post.from_dict(post_dict)
    assert post1 == post2
