from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import *


class NewsAdmin(admin.ModelAdmin):
    """
    Класс содержит аргументы, которые будут влиять на
    форму отображения таблицы в админ-панели
    """
    list_display = ('id', 'title', 'author', 'get_image', 'is_published')  # Отображаемые поля
    list_display_links = ('id', 'title')  # Кликабельные поля
    search_fields = ('title', 'content', 'author', 'time_create', 'time_update')  # Поля, по которым возможен поиск
    list_editable = ('is_published',)  # Редактируемые поля

    # prepopulated_fields = {'slug': ('title',)}  # Для автозаполнения поля slug по названию title

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=70>")

    get_image.short_description = 'Миниатюра'


class NewsCommentsAdmin(admin.ModelAdmin):
    """
    Класс содержит аргументы, которые будут влиять на
    форму отображения таблицы в админ-панели
    """
    list_display = ('id', 'news_id', 'content', 'author', 'time_create')  # Отображаемые поля
    list_display_links = ('id', 'content')  # Кликабельные поля
    search_fields = ('news_id', 'author')  # Поля, по которым возможен поиск


class NewsLikesAdmin(admin.ModelAdmin):
    """
    Класс содержит аргументы, которые будут влиять на
    форму отображения таблицы в админ-панели
    """
    list_display = ('id', 'news_id', 'author',)  # Отображаемые поля
    list_display_links = ('id',)  # Кликабельные поля
    search_fields = ('news_id', 'author')  # Поля, по которым возможен поиск


admin.site.register(News, NewsAdmin)  # Регистрируем таблицу и созданный выше класс  для отображения в админ-панели
admin.site.register(NewsLikes, NewsLikesAdmin)  # Регистрируем таблицу и созданный выше класс
admin.site.register(NewsComments, NewsCommentsAdmin)  # Регистрируем таблицу и созданный выше класс
