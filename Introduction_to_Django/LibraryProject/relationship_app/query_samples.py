import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author name.
    """
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author named {author_name}")
        return []
    books = list(author.books.all())  
    print(f"Books by {author_name}:")
    for b in books:
        print(f" - {b.title}")
    return books


def list_books_in_library(library_name):
    """
    List all books in a library by library name.
    """
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named {library_name}")
        return []
    books = list(lib.books.all())
    print(f"Books in library '{library_name}':")
    for b in books:
        print(f" - {b.title} (author: {b.author.name})")
    return books


def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named {library_name}")
        return None

    try:
        librarian = lib.librarian
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")
        return None

    print(f"Librarian for library '{library_name}': {librarian.name}")
    return librarian


if __name__ == '__main__':
    query_books_by_author('Jane Austen')
    list_books_in_library('City Library')
    get_librarian_for_library('City Library')
