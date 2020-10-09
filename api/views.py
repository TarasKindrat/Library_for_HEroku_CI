from authentication.models import CustomUser
from order.models import Order
from author.models import Author
from book.models import Book
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer
from .serializers import OrderSerializer
from .serializers import AuthorSerializer
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

# return 404 status code



class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.request.GET.get("pk")
        order = Order.objects.all()
        #order = Order.objects.get(pk=pk)
        print(order)
        return order



@api_view(['GET'])
def orderDetail_dec(request, id):
    try:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order.to_dict())
        return Response(serializer.data)
    except Exception as e:
        return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def orderUpdate(request, id):
    try:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def orderDelete(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return Response("Order Deleted Successfully")
    except:
        return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)



def login_redirect(request):
    return redirect('/api/v1/')



