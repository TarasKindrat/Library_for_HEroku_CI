from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

def index(request):
    return HttpResponse('<h1>Start for book.</h1>')

def get_book_by_id(request, id=0):
    context = {'book_by_id': Book.get_by_id(id)}
    return render(request, 'book/get_book_by_id.html', context)

def get_all_books(request):
    context = {'book_list': Book.get_all()}
    return render(request, 'book/book_list.html', context)