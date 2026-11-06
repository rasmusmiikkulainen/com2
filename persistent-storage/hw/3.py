try:
    filename = input("please enter filename: ")
    with open(filename, "r") as f:
        integers = [int(i) for i in f]
    print(sum(integers) / len(integers))
except Exception as e:
    print("exception:", e)
