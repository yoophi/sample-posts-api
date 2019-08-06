from flask import jsonify, request

from app.api import api
from app.repositories import current_repo
from app.core.request_objects.post import (
    PostListRequestObject,
    PostItemRequestObject,
    PostCreateRequestObject,
)
from app.core.use_cases import PostListUseCase, PostItemUseCase, PostCreateUseCase
from app.serializers import PostSchema


@api.route("/v1/posts", methods=["GET"])
def post_list():
    """
    Post 목록
    ---
    tags:
    - post
    responses:
      200:
        description: "Success"
        schema:
          type: "array"
          items:
            $ref: "#/definitions/Post"
    """

    req = PostListRequestObject()
    uc = PostListUseCase(repo=current_repo)
    resp = uc.execute(req)

    if resp:
        schema = PostSchema(many=True, exclude=("comments",))
        posts = schema.dump(resp.value).data
        return jsonify(posts)
    else:
        return jsonify({}), 400


@api.route("/v1/posts", methods=["POST"])
def post_create():
    """
    새로운 Post 등록
    ---
    tags:
    - post
    parameters:
    - in: "body"
      name: "body"
      description: "Pet object that needs to be added to the store"
      required: true
      schema:
        $ref: "#/definitions/PostInput"
    responses:
      201:
        description: "생성됨"
      403:
        description: "권한 없음"
      405:
        description: "Invalid input"
    """
    payload = request.get_json()
    req = PostCreateRequestObject.from_dict(
        {"title": payload.get("title"), "body": payload.get("body")}
    )
    uc = PostCreateUseCase(repo=current_repo)
    resp = uc.execute(req)

    if resp:
        schema = PostSchema()
        post = schema.dump(resp.value).data
        return jsonify(post)
    else:
        return jsonify({}), 500


@api.route("/v1/posts/<post_id>", methods=["GET"])
def post_item(post_id):
    """
    Post 조회
    ---
    tags:
    - post
    parameters:
    - in: "path"
      name: "post_id"
      description: "게시물 번호"
      required: true
      type: "integer"
    responses:
      200:
        description: "성공"
        schema:
          $ref: "#/definitions/Post"
      403:
        description: "게시물 조회 권한이 없음"
      404:
        description: "게시물이 존재하지 않음"
    """

    req = PostItemRequestObject.from_dict({"id": int(post_id)})
    uc = PostItemUseCase(repo=current_repo)
    resp = uc.execute(req)

    if resp:
        schema = PostSchema()
        post = schema.dump(resp.value).data
        return jsonify(post)
    elif resp.type == "NotFoundError":
        return jsonify({}), 404
    else:
        return jsonify({}), 500


@api.route("/v1/posts/<post_id>", methods=["PUT"])
def post_update(post_id):
    """
    Post 수정
    ---
    tags:
    - post
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


@api.route("/v1/posts/<post_id>", methods=["DELETE"])
def post_delete(post_id):
    """
    Post 삭제
    ---
    tags:
    - post
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
