class Point(object):
    def __init__(self, x, y):
        self.x = float(x);
        self.y = float(y);

    def get_point(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** (float(1)/2)

