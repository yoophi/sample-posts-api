import json

from app.domain.comment import Comment
from app.serializers import CommentSchema


def test_serialize_domain_comment():
    comment = Comment(id=1, body="body text")

    expected_json = """
    {
      "id": 1,
      "body": "body text"
    }
    """

    json_comment = CommentSchema().dump(comment).data

    assert json_comment == json.loads(expected_json)
