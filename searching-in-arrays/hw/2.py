students = ["Alissa", "Ben", "Charlie", "Dianna"]
grades = ["B", "D", "B", "A"]

key = "Charlie"
found = False
for i in range(len(students)):
    if students[i] == key:
        found = True
        break
if found:
    print(grades[i])
else:
    print(f"{key} not found")
