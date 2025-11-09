# Retrieve and display all attributes of the book just created.
Book.objects.get, "1984"

print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.year)

