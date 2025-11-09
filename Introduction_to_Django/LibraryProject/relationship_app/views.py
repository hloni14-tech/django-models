from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def hello_view(request):
    return HttpResponse

def book_list(request):
    books = Book.objects.all()

    context ={'book_list': books}
    return render(request,'books/book_list.html',context)

from django.views.from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.get_average_rating()


