class Project:
    current_id = 0

    def __init__(self, tasks):
        self.tasks = tasks
        self.id = Project.current_id
        Project.current_id += 1

    def __str__(self):
        return f"project {self.id}:\n" + "\n".join(
            [f"{i}. {task}" for i, task in enumerate([str(task) for task in self.tasks], 1)]
        )

class Task:
    def __init__(self, name, workers):
        self.name = name
        self.workers = workers

    def __str__(self):
        return f"{self.name} ({", ".join([str(worker) for worker in self.workers])})"

class Worker:
    def __init__(self, name):
        self.name = name

class Employee(Worker):
    def __str__(self):
        return f"employee {self.name}"

class Contractor(Worker):
    def __str__(self):
        return f"contractor {self.name}"

print(
    Project(
        [
            Task("cleaning", [Contractor("John"), Employee("Mary")]),
            Task("cooking", [Contractor("Mike"), Employee("Jane")])
        ])
    )
