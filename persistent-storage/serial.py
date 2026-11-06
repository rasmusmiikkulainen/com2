class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

import pickle, pathlib # pickle for storage, hehe
file_path = pathlib.Path('persistent-storage') / "data" / 'points.ser' # file on drive
points_written = [Point(x, x**2) for x in range(20)] # some data
print(points_written[-1]) # last point written

# serialize / pickle onto drive
f = open(file_path, 'wb') # open file for writing binary data
pickle.dump(points_written, f) # save data into file
f.close() # close file

# deserialize / unpickle from drive
f = open(file_path, 'rb') # open for reading binary data
points_read = pickle.load(f) # read and return data
f.close() # close file
print(points_read[-1]) # last point read
