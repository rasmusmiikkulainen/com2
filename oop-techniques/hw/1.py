class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)


clrs = Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009)
book1 = Book("1984", ["Orwell"], 1949)
book2 = Book("Just for fun", ["Diamond", "Torvalds"], 2001)

books = [book2, book1, clrs]

def print_books(books):
    for b in books:
        print(b)

print_books(books)

books.sort(key=Book.num_authors, reverse=True)
print("SORTED")

print_books(books)
