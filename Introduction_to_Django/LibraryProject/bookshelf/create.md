# Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
Book.objects.create

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Create an instance of Book
book = Book(title="1984", author="George Orwell", year=1949)

# Display confirmation of creation
print(f"Book created: {book.title} by {book.author}, published in {book.year}")

