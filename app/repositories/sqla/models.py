from datetime import datetime

from app.core.domain.comment import Comment
from app.core.domain.post import Post
from .database import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(255))
    body = db.Column(db.UnicodeText())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_entity(self):
        return Post.from_dict(
            {
                "id": self.id,
                "title": self.title,
                "body": self.body,
                "comments": [c.to_dict() for c in self.comments],
            }
        )


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.UnicodeText)

    post_id = db.Column(db.Integer, db.ForeignKey(PostModel.id))
    post = db.relationship(PostModel, backref="comments")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {"id": self.id, "post_id": self.post_id, "body": self.body}

    def to_entity(self):
        return Comment.from_dict(
            {"id": self.id, "post_id": self.post_id, "body": self.body}
        )
