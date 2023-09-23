from django.db import models


class Book(models.Model):
    image = models.ImageField(
        'Картинка книги',
        upload_to='books/'
    )
    book_title = models.CharField(
        'Название книги',
        max_length=None
    )
    book_categories = models.CharField(
        'Категория книги',
        max_length=None,
    )
    number_of_pages = models.PositiveIntegerField(
        'Количество страниц',
    )
    book_number = models.PositiveIntegerField(
        'Артикул книги',
        unique=True,
    )
    # добавить категорию Новинки
    # new_books = models.models.ForeignKey(
        # Book,
        # on_delete=models.CASCADE
    # )
    # books_from_the_category = models.CharField(
        # 'Книги из текущей категории'
    # )
    # recommendations = 

    class Meta:
        # ordering = ['-pub_date']
        default_related_name = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.book_title


class Category(models.Model):
    category = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    # добавить категорию Новинки
    # new_books = models.models.ForeignKey(
        # Book,
        # on_delete=models.CASCADE
    # )

    class Meta:
        # ordering = ['-pub_date']
        default_related_name = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category