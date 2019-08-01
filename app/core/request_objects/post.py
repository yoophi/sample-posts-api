from marshmallow import fields, validates, ValidationError
from voluptuous import Schema, Required, All, MultipleInvalid

from app.core.request_objects import ValidRequestObject, InvalidRequestObject
from app.extensions import ma
from app.swagger import swagger_definition

validate_post_item_request_object = Schema({Required("id"): All(int)})


class PostListRequestObject(ValidRequestObject):
    @classmethod
    def from_dict(cls, _):
        return cls()


class PostItemRequestObject(ValidRequestObject):
    def __init__(self, id):
        self.id = id

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        try:
            validate_post_item_request_object(adict)
        except MultipleInvalid as exc:
            for error in exc.errors:
                invalid_req.add_error("validation", str(error))

        if invalid_req.has_errors():
            return invalid_req

        return cls(**adict)


class PostCreateRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        result, errors = ValidatePostInputSchema().load(kwargs)
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
        return {"title": self.title, "body": self.body}


@swagger_definition
class ValidatePostInputSchema(ma.Schema):
    """
    PostInput
    ---
    type: "object"
    properties:
      title:
        type: "string"
      body:
        type: "string"
    """

    title = fields.String(required=True)
    body = fields.String(required=True)

    @validates("title")
    def validate_title(self, value):
        value = value.strip()
        if not len(value) > 0:
            raise ValidationError("Title must not be empty.")

    @validates("body")
    def validate_body(self, value):
        value = value.strip()
        if not len(value) > 0:
            raise ValidationError("Title must not be empty.")
