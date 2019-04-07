class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_xy(self):
        return (self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)