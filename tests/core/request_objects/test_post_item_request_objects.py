from app.core.request_objects.post import PostItemRequestObject


def test_build_post_item_request_object_from_empty_dict():
    request = PostItemRequestObject.from_dict({})

    assert bool(request) is False
