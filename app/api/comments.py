from flask import request, jsonify

from app.repositories import current_repo
from app.core.request_objects.comment import CommentCreateRequestObject
from app.serializers import CommentSchema
from app.core.use_cases import CommentCreateUseCase
from . import api


@api.route("/v1/posts/<post_id>/comments", methods=["GET"])
def comment_list(post_id):
    """
    Post 에 대한 Comment 목록
    ---
    tags:
    - comment
    parameters:
    - in: "body"
      name: "body"
      description: "Pet object that needs to be added to the store"
      required: true
      schema:
        $ref: "#/definitions/Post"
    responses:
      405:
        description: "Invalid input"
    """
    return {}


@api.route("/v1/posts/<post_id>/comments", methods=["POST"])
def comment_create(post_id):
    """
    Comment 등록
    ---
    tags:
    - comment
    parameters:
    - in: "path"
      name: "post_id"
      description: "게시물 번호"
      required: true
      type: "integer"
    - in: "body"
      name: "body"
      description: "Pet object that needs to be added to the store"
      required: true
      schema:
        $ref: "#/definitions/CommentInput"
    responses:
      405:
        description: "Invalid input"
    """
    payload = request.get_json()
    req = CommentCreateRequestObject.from_dict({"post_id": int(post_id), **payload})
    uc = CommentCreateUseCase(repo=current_repo)
    resp = uc.execute(req)

    if resp:
        schema = CommentSchema()
        rv = schema.dump(resp.value).data
        return jsonify(rv)
    else:
        return jsonify({}), 500


@api.route("/v1/posts/<post_id>/comments/<comment_id>", methods=["DELETE"])
def comment_delete(post_id, comment_id):
    """
    Comment 삭제
    ---
    tags:
    - comment
    parameters:
    - in: "body"
      name: "body"
      description: "Pet object that needs to be added to the store"
      required: true
      schema:
        $ref: "#/definitions/Post"
    responses:
      405:
        description: "Invalid input"
    """
    return {}


@api.route("/v1/posts/<post_id>/comments/<comment_id>", methods=["PUT"])
def comment_update(post_id, comment_id):
    """
    ---
    tags:
    - comment
    parameters:
    - in: "body"
      name: "body"
      description: "Pet object that needs to be added to the store"
      required: true
      schema:
        $ref: "#/definitions/Post"
    responses:
      405:
        description: "Invalid input"
    """
    return {}
