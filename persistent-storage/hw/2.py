# float("hello")

while True:
    try:
        value = float(input("please enter float: "))
        break
    except ValueError:
        print("please enter valid float")
