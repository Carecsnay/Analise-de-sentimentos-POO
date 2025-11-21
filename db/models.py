class Post:
    def __init__(self, post, id=None, category=None, active=True, score=None):
        self.id = id
        self.post = post
        self.category = category
        self.active = active
        self.score = score