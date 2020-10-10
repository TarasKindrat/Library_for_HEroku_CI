from api import views
from rest_framework import routers
from django.urls import path, include
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'user', views.CustomUserViewSet)
router.register(r'order', views.OrdersViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
#router.register(r'user/(?P<<id.+>)/order', OrdersViewSet)

urlpatterns = [
    #path('api/v1/', include('rest_framework.urls', namespace='rest_framework'))
    path('',  include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/<int:pk>/order/', views.OrderDetail.as_view(), name='order_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.login_redirect, name='login_redirect'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login')
    # path('user/<int:id>/order/', views.orderDetail_dec, name='order_detail'),
    # path('user/<int:id>/order/update', views.orderUpdate, name='order_detail'),
    # path('user/<int:id>/order/delete', views.orderDelete, name='order_detail'),

]