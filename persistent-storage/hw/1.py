import random, pathlib, pickle

integers = [random.randint(0, 10000) for _ in range(10000)]
print(integers[-1])

txt_path = pathlib.Path("persistent-storage") / "data" / "hw1.txt"
ser_path = pathlib.Path("persistent-storage") / "data" / "hw1.ser"

if not txt_path.exists():
    with open(txt_path, "w") as f:
        for i in integers:
            print(i, file=f)

if not ser_path.exists():
    with open(ser_path, "wb") as f:
        pickle.dump(integers, f)

with open(ser_path, "rb") as f:
    ser_integers = pickle.load(f)

print("from ser:", ser_integers[-1])

with open(txt_path, "r") as f:
    txt_integers = [int(line) for line in f]

print("from txt:", txt_integers[-1])
