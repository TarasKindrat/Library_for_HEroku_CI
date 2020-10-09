from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order
from authentication.models import CustomUser
from book.models import Book

def index(request):
    return HttpResponse('<h1>Start for orders.</h1>')


def get_all_orders(request):
    ol = list(Order.get_all())

    usrs =  [CustomUser.get_by_id(order.user_id) for order in ol]
    return render(request, 'order/get_all.html', context={'orders_list': ol, 'users': usrs})


def get_order_by_id(request, id=0):

    order_found = Order.get_by_id(id)
    usr = CustomUser.get_by_id(order_found.user_id)
    bk = Book.get_by_id(order_found.book_id)
    al = [authors for authors in list(bk.authors.all())]
    return render(request, 'order/get_order_by_id.html', context = {'order': order_found, 'user': usr, 'book': bk, 'authors_list': al})