class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, value):
        if value == (self.x, self.y):
            return True
        return False

    def on_x(self):
        if self.y == 0:
            return True
        return False

    def dist(self, point):
        return ( (self.x - point.x) ** 2 + (self.y - point.y) ** 2 ) ** 0.5

    def in_unit_circle(self):
        if self.dist(Point(0, 0)) <= 1:
            return True
        return False

    def midpoint(self, point):
        return Point((self.x + point.x) / 2, (self.y + point.y) / 2)

import random

point_range = 1000
val = 500

buncha_points = [Point(random.randint(-point_range, point_range), random.randint(-point_range, point_range)) for _ in range(100)]
best_points = [point.midpoint(buncha_points[0]) for point in buncha_points[1:] if buncha_points[0].dist(point) < val]

for point in best_points:
    if point == Point(0, 0):
        print(point + "\nvery good")
        break
    elif point.in_unit_circle():
        print("almost")

print(buncha_points[0])
print(len(best_points))
