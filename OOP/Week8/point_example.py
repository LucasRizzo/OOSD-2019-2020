import math


class Point(object):
    def __init__(self, x_param = 0.0, y_param = 0.0):
        self.x = x_param
        self.y = y_param

    def distance(self, param_pt):
        x_diff = self.x - param_pt.x # x1 - x2
        y_diff = self.y - param_pt.y # y1 - y2
        return math.sqrt(x_diff**2 + y_diff**2)

    def sum(self, param_pt):
        # new_pt = Point()
        # new_pt.x = self.x + param_pt.x
        # new_pt.y = self.y + param_pt.y
        # return new_pt
        return Point(self.x + param_pt.x, self.y + param_pt.y)

    def __str__(self):
        return "{:.2f}, {:.2f}".format(self.x, self.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.x)

p3 = p1.sum(p2)

print(p3)

