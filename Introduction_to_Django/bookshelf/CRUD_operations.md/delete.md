# Delete the book instance and confirm deletion by attempting to retrieve it again.

del book

try:
    print(book.title)
except NameError:
    print("Book not found. It has been successfully deleted.")
