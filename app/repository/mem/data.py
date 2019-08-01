import random

from faker import Faker

fake = Faker()

posts = [
    {"id": id_, "title": fake.sentence(), "body": fake.text()} for id_ in range(1, 100)
]
comments = [
    {"id": id_, "post_id": random.choice(range(1, 100)), "body": fake.text()} for id_ in range(1, 300)
]

initial_data = {"posts": posts, "comments": comments, }
