from app.core.request_objects.comment import CommentCreateRequestObject


def test_build_comment_create_request_object_from_empty_dict():
    request = CommentCreateRequestObject.from_dict({})

    assert bool(request) is False


def test_build_comment_create_request_object_from_valid_dict():
    request = CommentCreateRequestObject.from_dict(
        {"post_id": 1, "title": "title", "body": "body text"}
    )

    assert bool(request) is True
    assert request.title == "title"
    assert request.body == "body text"
