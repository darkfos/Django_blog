from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Модель таблицы Post в админке
    """

    #Показ определённых полей модели
    list_display = ["title", "slug", "body", "publish_date", "status"]

    #Фильтр поиска
    list_filter = ["status", "created_date", "publish_date", "user_id"]

    #Поисковик по полям
    search_fields = ["title", "body"]

    #Предопределение для поля, постановка записи из title
    prepopulated_fields = {"slug": ("title",)}

    #ID таблицы User
    raw_id_fields = ["user_id"]

    #Навигация - ссылки
    date_hierarchy = "publish_date"

    #Упорядочивание
    ordering = ["status", "publish_date"]