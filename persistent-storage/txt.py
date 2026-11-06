class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

import pathlib
file_path = pathlib.Path('data') / 'points.txt'
points_written = [Point(x, x**2) for x in range(20)] # some data
# write data onto drive: x y on each line
f = open(file_path, 'w') # open file for writing (text) data
for p in points_written: print(p.x, p.y, file=f) # print data
f.close() # close file

# read data from file
f = open(file_path) # open file (for reading text)
points_read = []
for line in f: # iterate over lines
    [x, y] = [int(word) for word in line.split()] # extract x, y
    points_read.append(Point(x, y))
f.close() # close file
print(points_written[-1], points_read[-1]) # check against orig
