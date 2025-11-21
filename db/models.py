class Post:
    def __init__(self, post, category=None, active=True, score=None):
        self.post = post
        self.category = category
        self.active = active
        self.score = score