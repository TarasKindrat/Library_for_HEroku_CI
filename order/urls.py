from django.urls import  path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all/', views.get_all_orders, name='get_all'),
    path('get_by_id/<int:id>/', views.get_order_by_id, name='get_order_by_id'),
]