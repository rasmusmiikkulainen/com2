class Newspaper:
    def __init__(self, __name, year, month, day_of_month, is_finnish):
        self.name = __name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def get_name(self):
        return self.name

    def __str__(self):
        return "\n".join([f"{"finnish" if self.is_finnish else "bad"} newspaper {self.name}",
                f"date of publication: {self.day_of_month}.{self.month}.{self.year}"])

# print(Newspaper("HS", 1917, 6, 12, True))
# print(Newspaper("The Guardian", 2026, 3, 11, False))

options = [Newspaper("HS", 1917, 6, 12, True),
           Newspaper("The Guardian", 2026, 11, 3, False),
           Newspaper("IS", 2026, 11, 3, True)]

today = (3, 11, 2026)

# get finnish newspaper names that were published today
news = [n.name for n in options
        if (n.is_finnish and (n.day_of_month, n.month, n.year) == today)]

print(", ".join(news))
