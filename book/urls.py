from django.urls import  path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_by_id/<int:id>/', views.get_book_by_id, name='get_book_by_id'),
    path('get_all/', views.get_all_books, name='book_list'),
]