from rest_framework import serializers
from authentication.models import CustomUser
from order.models import Order
from author.models import Author
from book.models import Book


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "middle_name", "last_name", "email", "password", "updated_at", "created_at",
                  "role", "is_active", "is_staff")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "user", "book", "created_at", "end_at", "plated_end_at")


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id",  "name", "surname", "patronymic")


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id",  "name", "description", "count", "authors")





