from app.domain.comment import Comment


class Post:
    def __init__(self, id=None, title=None, body=None, comments=None):
        self.id = id
        self.title = title
        self.body = body

        if comments is None:
            comments = []

        self.comments = [Comment.from_dict(d) for d in comments]

    @classmethod
    def from_dict(cls, adict):
        kwargs = {"id": adict["id"], "title": adict["title"], "body": adict["body"], "comments": adict.get("comments", [])}
        return cls(**kwargs)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "body": self.body, "comments": [
            c.to_dict() for c in self.comments
        ]}

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
