from django.urls import  path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all/', views.get_all_authors, name='author_list'),
    path('get_by_id/<int:id>/', views.get_author_by_id, name='get_author_by_id'),
]