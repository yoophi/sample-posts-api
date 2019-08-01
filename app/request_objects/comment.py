from marshmallow import fields, validates, ValidationError

from app.extensions import ma
from app.request_objects import ValidRequestObject, InvalidRequestObject
from app.swagger import swagger_definition


class CommentListRequestObject(ValidRequestObject):
    @classmethod
    def from_dict(cls, adict):
        pass


@swagger_definition
class ValidateCommentInputSchema(ma.Schema):
    """
    CommentInput
    ---
    type: "object"
    properties:
      body:
        type: "string"
    """

    post_id = fields.Integer(required=True)
    body = fields.String(required=True)

    @validates("body")
    def validate_body(self, value):
        value = value.strip()
        if not len(value) > 0:
            raise ValidationError("Title must not be empty.")


class CommentCreateRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        result, errors = ValidateCommentInputSchema().load(kwargs)
        if errors:
            raise ValidationError(message=str(errors))

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def from_dict(cls, adict):
        try:
            return cls(**adict)
        except ValidationError:
            return InvalidRequestObject()

    def to_dict(self):
        return {"post_id": self.post_id, "body": self.body}
