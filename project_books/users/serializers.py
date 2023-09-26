from re import match

from django.conf import settings
from djoser.serializers import UserSerializer
from rest_framework.serializers import ValidationError

from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    """Кастомный сериализатор для работы с пользователями."""

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'name',
            'message',
            'phone',
        )

    # def validate_email(self, value):
    #     if not match(r'[\w.@+\-]+', value):
    #         raise ValidationError('Некорректный email.')
    #     return value

    def validate_email(self, value):
        email = value.lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Такой электронный адрес уже существует.')
        return email

    def validate_name(self, value):
        if not match(settings.NAME_REGEX_PATTERN, value):
            raise ValidationError('Некорректное имя пользователя.')
        return value

    # def validate_message(self, value):
    #     if not match(settings.PHONE_NUMBER_REGEX, value):
    #         raise ValidationError('')
    #     return value

    def validate_phone(self, value):
        if not match(settings.PHONE_NUMBER_REGEX, value):
            raise ValidationError('Некорректный номер телефона.')
        return value
