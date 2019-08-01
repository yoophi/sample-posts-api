from app.domain.comment import Comment


def test_comment_model_init():
    id_ = 1
    comment = Comment(id_, body="body text")
    assert comment.id == id_
    assert comment.body == "body text"


def test_comment_model_from_dict():
    comment = Comment.from_dict({"id": 1, "body": "body text"})

    assert comment.id == 1
    assert comment.body == "body text"


def test_comment_model_to_dict():
    comment_dict = {"id": 1, "body": "body text"}

    comment = Comment.from_dict(comment_dict)

    assert comment.to_dict() == comment_dict
