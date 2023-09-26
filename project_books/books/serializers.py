import base64
from re import match

from django.conf import settings
from django.core.files.base import ContentFile
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import (CurrentUserDefault, HiddenField,
                                        ImageField, ModelSerializer,
                                        SerializerMethodField, ValidationError)

from books.models import Book


class Base64ImageField(ImageField):
    """Класс для добавления добавления картинки книги."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
        return super().to_internal_value(data)


class BookSerializer(ModelSerializer):
    """Кастомный сериализатор для работы с книгами."""
    image = Base64ImageField()

    class Meta:
        model = Book
        fields = (
            'image',
            'book_title',
            'book_categories',
            'number_of_pages',
            'book_number'
        )


class CategorySerializer(ModelSerializer):
    """Кастомный сериализатор для работы с категориями."""

    class Meta:
        model = Book
        fields = (
            'category',
            'subcategory',
            'status',
        )
