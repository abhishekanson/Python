class Publisher:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Publisher: {self.name}")


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def show(self):
        super().show() 
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

book = Book("Pearson", "Python Programming", "Mark Lutz")

print("\n--- Book Details ---")
book.show()
