from app.core.base.base_repository import BaseRepository
from app.repositories.sqla.database import db
from app.repositories.sqla.models import PostModel, CommentModel


class SqlaRepo(BaseRepository):
    def get_post_list(self):
        result = db.session.query(PostModel)
        return [model.to_entity() for model in result]

    def get_post_item(self, id):
        post = db.session.query(PostModel).get(id)

        if not post:
            return None
        try:
            return post.to_entity()
        except Exception as e:
            raise e

    def create_post(self, adict):
        post = PostModel(title=adict["title"], body=adict["body"])
        db.session.add(post)
        db.session.commit()

        return post.to_entity()

    def create_comment(self, adict):
        comment = CommentModel(post_id=adict["post_id"], body=adict["body"])
        db.session.add(comment)
        db.session.commit()

        return comment.to_entity()
