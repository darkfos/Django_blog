from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    Таблица записи
    """

    class Status(models.TextChoices):
        """
        Статус пост, черновик или опубликован
        """

        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    #Атрибуты модели
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        """
        Определение метаданных модели Post
        сортировка значений таблица по полю publish_date
        Применяется, когда запросов на сортировку нет.
        """
        ordering = ["-publish_date"]

        #Индексирование по столбцу, повышает производительность
        indexes = [
            models.Index(fields=['-publish_date'])
        ]


    def __str__(self):
        """
        Строковое представление объекта Post
        :return:
        """
        return self.title