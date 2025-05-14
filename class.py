# Base class - Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def is_modern(self):
        current_year = 2025
        if current_year - self.year <= 10:
            return True
        return False

# Subclass - Ebook (inherits from Book)
class Ebook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size  # New attribute for Ebook

    def display_info(self):
        # Override display_info method for Ebook
        return f"'{self.title}' by {self.author}, published in {self.year}, File size: {self.file_size}MB"

# Create objects
book1 = Book("1984", "George Orwell", 1949)
ebook1 = Ebook("The Hobbit", "J.R.R. Tolkien", 1937, 5)

print(book1.display_info())
print(f"Is it modern? {'Yes' if book1.is_modern() else 'No'}")

print(ebook1.display_info())
