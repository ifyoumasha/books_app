from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """Mодель пользователя."""

    email = models.EmailField(
        'E-mail',
        unique=True,
        help_text=('Введите ваш e-mail'),
        # validators
    )
    name = models.CharField(
        'Имя',
        max_length=100,
        unique=True,
        help_text=('Введите ваше имя'),
        # validators=[username_validator],
    )
    message = models.TextField(
        'Сообщение',
        help_text=('Оставьте обратную связь'),
    )
    phone = PhoneNumberField(
        'Номер телефона',
        unique=True,
    )

    class Meta:
        ordering = ('id',)
        default_related_name = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
