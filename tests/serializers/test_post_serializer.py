import json

from app.domain.comment import Comment
from app.domain.post import Post
from app.serializers import PostSchema


def test_serialize_domain_post():
    post = Post(id=1, title="title", body="body text")

    expected_json = """
    {
      "id": 1,
      "title": "title",
      "body": "body text"
    }
    """

    json_post = PostSchema(exclude=("comments",)).dump(post).data

    assert json_post == json.loads(expected_json)


def test_serialize_domain_post_with_comments():
    post = Post(
        id=1,
        title="title",
        body="body text",
        comments=[dict(id=1, body="body one"), dict(id=2, body="body two")],
    )

    expected_json = """
    {
      "id": 1,
      "title": "title",
      "body": "body text",
      "comments": [
        { "id": 1, "body": "body one" },
        { "id": 2, "body": "body two" }
      ]
    }
    """

    json_post = PostSchema().dump(post).data

    assert json_post == json.loads(expected_json)
