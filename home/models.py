from django.db import models


class WebsiteFeatures(models.Model):
    """
    Модель содержит информацию о возможностях данного сайта.
    Эти данные будут использоваться для формирования стартовой страницы,
    а так же для формирования меню на главной странице
    """
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='features_img/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='URL адрес | Название иконки',
                            help_text='Указывается id иконки, содержащейся в файле static/main/img/sprite.svg. Также это поле используется в качестве слага при указании на URL страницу')

    def __str__(self):
        """ В запросах Qwerty отображается заголовки title для каждой строки таблицы """
        return self.title

    class Meta:
        """
        Подкласс указывает имена для отображения таблицы WebsiteFeatures в панели
        администратора и определяет по каким полям проводить сортировку
        """
        verbose_name = "Возможность сайта"
        verbose_name_plural = "Возможности сайта"
        ordering = ['id']
