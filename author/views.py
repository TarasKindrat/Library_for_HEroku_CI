from django.shortcuts import render
from django.http import HttpResponse
from author.models import Author
from book.models import Book

def index(request):
    return HttpResponse('<h1>Start for author.</h1>')

def get_all_authors(request):
    context = {'author_list': list(Author.get_all()), 'books': Book.get_all()}
    return render(request, 'author/author_list.html', context)

def get_author_by_id(request, id=0):
    author_by_id = Author.get_by_id(id)
    bks = [book for book in list(Book.get_all()) if author_by_id in book.authors.all()]
    # books = list(Book.get_all())
    return render(request, 'author/get_author_by_id.html', context = {'author_by_id': author_by_id, 'books': bks})