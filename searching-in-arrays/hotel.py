names = ["John", "Mary", "Diana"]
rooms = [111, 123, 111]

key = "Dave"

index = 0
found = False
while not found and index < len(names):
    if names[index] == key:
        found = True
    else:
        index += 1
if found:
    print(rooms[index])
else:
    print(f"{key} not a guest here")