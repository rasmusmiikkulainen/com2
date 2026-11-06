class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

try:
    import pathlib
    file_path = pathlib.Path("persistent-storage") / "data" / 'points.txt'
    with open(file_path) as f:
        points_read = []
        for line in f: # traverse lines
            # extract x, y
            [x, y] = [int(word) for word in line.split()]
            points_read.append(Point(x, y))
    print(points_read[-1])
except Exception as e: # handle any exception raised
    print('exception:', e)
