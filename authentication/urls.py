from django.urls import  path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('get_all/', views.get_all_users, name='get_all'),
    path('get_by_id/<int:id>/', views.get_user_by_id, name='get_user_by_id'),
    path('get_by_id/<int:id>/update/', views.edit_user, name="update_custom_user"),
    path('get_by_id/<int:id>/delete/', views.user_delete, name="delete_user"),
    url(r'^signup/$', views.signup, name='signup'),

]