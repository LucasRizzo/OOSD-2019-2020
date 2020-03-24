class Rectangle(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)


rectangle = Rectangle(10, 20)

print(str(rectangle.area()))
print(str(rectangle.perimeter()))
#
# import math
#
# class Point(object):
#     def __init__(self, x_param=0.0, y_param=0.0):  # create and initialise
#         self.x = x_param
#         self.y = y_param
#
#     def distance(self, param_pt):  # standard distance formula
#         """ Distance between self and a Point """
#         x_diff = self.x - param_pt.x  # (x1 − x2 )
#         y_diff = self.y - param_pt.y  # (y1 − y2 )
#         # square differences, sum, and take sqrt
#         return math.sqrt(x_diff ** 2 + y_diff ** 2)
#
#     def sum(self, param_pt):  # new point from vector sum
#         """ Vector Sum of self and a Point """
#         new_pt = Point()  # create a new point
#         new_pt.x = self.x + param_pt.x  # calculate x value sum from self and pt
#         new_pt.y = self.y + param_pt.y
#         return new_pt
#
#     def __str__(self):
#         """Print as a coordinate pair . """
#         print("called the str method")
#         return "({:.2f}, {:.2f})".format(self.x, self.y)
#
#
# class Rectangle(object):
#     def __init__(self,p1,p2,p3,p4):
#         self.p1 = p1
#         self.p2 = p2
#         self.p3 = p3
#         self.p4 = p4
#
#     def area(self):
#         return self.p1.distance(self.p2) * self.p2.distance(self.p3)
#
#     def perimeter(self):
#         return self.p1.distance(self.p2) + self.p2.distance(self.p3) +\
#                self.p3.distance(self.p4) + self.p4.distance(self.p1)
#
# p1 = Point(0, 0)
# p2 = Point(0, 1)
# p3 = Point(2, 1)
# p4 = Point(2, 0)
#
# rectangle = Rectangle(p1, p2, p3, p4)
#
# print (str(rectangle.area()))
# print (str(rectangle.perimeter()))
