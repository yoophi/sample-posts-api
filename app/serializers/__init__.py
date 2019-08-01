from marshmallow import fields

from app.extensions import ma
from app.swagger import swagger_definition


@swagger_definition
class PostSchema(ma.Schema):
    """
    Post
    ---
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      title:
        type: "string"
      body:
        type: "string"
      created_at:
        type: "string"
        format: "date-time"
    """

    class Meta:
        fields = ("id", "title", "body", "comments")

    comments = fields.Nested("CommentSchema", many=True)


@swagger_definition
class CommentSchema(ma.Schema):
    """
    Comment
    ---
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      body:
        type: "string"
      created_at:
        type: "string"
        format: "date-time"
    """

    class Meta:
        fields = ("id", "body")
