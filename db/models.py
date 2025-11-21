class Post:
    def __init__(self, post, category=None, active=True):
        self.post = post
        self.category = category
        self.active = active