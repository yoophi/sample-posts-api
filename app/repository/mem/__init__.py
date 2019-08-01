from collections import defaultdict

from app.domain.comment import Comment
from app.domain.post import Post


class MemRepo:
    def __init__(self, data):
        self._data = defaultdict(list)

        for k, v in data.items():
            self._data[k].extend(v)

    def post_list(self):
        result = [Post.from_dict(d) for d in self._data["posts"]]

        return result

    def post_item(self, id):
        filtered = list(filter(lambda d: d["id"] == id, self._data["posts"]))

        if not filtered:
            return None

        post_dict = filtered[0]
        post_dict["comments"] = list(filter(lambda d: d["post_id"] == id, self._data["comments"]))
        return Post.from_dict(post_dict)

    def post_create(self, adict):
        next_id = self._get_max_id("posts") + 1
        adict["id"] = next_id

        self._data["posts"].append(adict)

        return Post.from_dict(adict)

    def _get_max_id(self, key):
        ids = [item["id"] for item in self._data[key]]
        if not ids:
            return 0

        return max(ids)

    def comment_create(self, adict):
        next_id = self._get_max_id("comments") + 1
        adict["id"] = next_id

        self._data["comments"].append(adict)

        return Comment.from_dict(adict)
