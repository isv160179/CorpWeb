from django.db import models
from django.urls import reverse

from CorpWebsite import settings


class News(models.Model):
    """
    Модель содержит информацию о новостях, размещенных пользователями.
    """
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст новости')
    image = models.ImageField(upload_to='news_img/%Y/%m/%d', blank=True, verbose_name='Изображение')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='authors_news', null=True, blank=True,
                               on_delete=models.SET_DEFAULT, default=1,
                               verbose_name='Автор новости')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Актуальность')
    users_love = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='news_loves', blank=True)

    def __str__(self):
        """ В запросах Qwerty отображается заголовки title для каждой строки таблицы """
        return self.title

    def get_absolute_url(self, *args):
        """ Формирует маршрут к конкретной записи.
        Берется атрибут pk текущего экземпляра класса (новости)
        и передается в качестве значения словаря в urls.py для
        формирования маршрута с именем news по шаблону path('main/<int:news_id>/', show_news, name='main')
        """
        return reverse('news_detail', kwargs={'news_id': self.pk})
        # return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        """
        Подкласс указывает имена для отображения таблицы WebsiteFeatures в панели
        администратора и определяет по каким полям проводить сортировку
        """
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['time_create']


class NewsComments(models.Model):
    """
        Модель содержит информацию о комментариях к новостям.
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Комментируемая новость', related_name='news_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='authors_comments', null=True, blank=True,
                               on_delete=models.SET_DEFAULT, default=1,
                               verbose_name='Автор комментария')
    content = models.TextField(max_length=300, verbose_name='Текст комментария')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['news_id', '-time_create']


class NewsLikes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Понравившаяся новость', related_name='news_likes') 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='authors_likes', on_delete=models.CASCADE,
                               verbose_name='Кому понравилась новость')

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        ordering = ['news_id']
