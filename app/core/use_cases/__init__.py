from app.repositories import current_repo
from app.core.response_objects import ResponseFailure, ResponseSuccess


class PostItemUseCase:
    def __init__(self, repo=current_repo):
        self.repo = repo

    def execute(self, request_object):
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(request_object)

        try:
            result = self.repo.get_post_item(request_object.id)

            if result is None:
                return ResponseFailure.build_not_found_error(
                    "{}: {}".format("NotFoundError", "Resource not found.")
                )

            return ResponseSuccess(result)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )


class PostListUseCase:
    def __init__(self, repo=current_repo):
        self.repo = repo

    def execute(self, request_object):
        try:
            result = self.repo.get_post_list()
            return ResponseSuccess(result)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )


class PostCreateUseCase:
    def __init__(self, repo=current_repo):
        self.repo = repo

    def execute(self, request_object):
        try:
            result = self.repo.create_post(request_object.to_dict())
            return ResponseSuccess(result)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )


class PostDeleteUseCase:
    pass


class CommentListUseCase:
    pass


class CommentDeleteUseCase:
    pass


class CommentCreateUseCase:
    def __init__(self, repo=current_repo):
        self.repo = repo

    def execute(self, request_object):
        try:
            result = self.repo.create_comment(request_object.to_dict())
            return ResponseSuccess(result)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )
