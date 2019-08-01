class Comment:
    def __init__(self, id=None, post_id=None, body=None):
        self.id = id
        self.post_id = post_id
        self.body = body

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)

    def to_dict(self):
        return {"id": self.id, "body": self.body}

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
