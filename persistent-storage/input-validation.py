completed = False

while not completed:
    try:
        filename = input("enter filename: ")
        with open(filename, "at") as f:
            print(440, file=f)
        completed = True
    except Exception as e:
        print("exception:", e)
