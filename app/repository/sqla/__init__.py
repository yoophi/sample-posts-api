from app.repository.sqla.database import db
from app.repository.sqla.models import Post, Comment


class SqlaRepo:
    def post_list(self):
        result = db.session.query(Post)
        return [model.to_entity() for model in result]

    def post_item(self, id):
        post = db.session.query(Post).get(id)

        if not post:
            return None
        try:
            return post.to_entity()
        except Exception as e:
            raise e

    def post_create(self, adict):
        post = Post(title=adict['title'], body=adict['body'])
        db.session.add(post)
        db.session.commit()

        return post.to_entity()

    def comment_create(self, adict):
        comment = Comment(post_id=adict["post_id"], body=adict["body"])
        db.session.add(comment)
        db.session.commit()

        return comment.to_entity()
