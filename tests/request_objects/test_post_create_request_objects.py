from app.request_objects.post import PostItemRequestObject, PostCreateRequestObject


def test_build_post_create_request_object_from_empty_dict():
    request = PostCreateRequestObject.from_dict({})

    assert bool(request) is False


def test_build_post_create_request_object_from_valid_dict():
    request = PostCreateRequestObject.from_dict({"title": "title", "body": "body text"})

    assert bool(request) is True
    assert request.title == "title"
    assert request.body == "body text"
