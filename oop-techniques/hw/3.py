class Class:
    def __init__(self, name, topic, teacher, num_of_participants):
        self.name = name
        self.topic = topic
        self.teacher = teacher
        self.num_of_participants = num_of_participants

period = [
    Class("COM2.e", "Computer Science", "Jarmo Hurri", 15),
    Class("MAA5", "Mathematics", "Niina Anjala", 20),
    Class("CS2", "Counter Strike", "ropz", 10)
]

# list of possible courses for a classroom of this size
classroom_size = 18

possibilities = [f"{c.teacher}: {c.name}, {c.topic}"
                 for c in period if c.num_of_participants <= classroom_size]

print(possibilities)
