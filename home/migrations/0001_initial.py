# Generated by Django 4.0.6 on 2022-07-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.CharField(max_length=150, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='features_img/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('slug', models.SlugField(help_text='Указывается id иконки, содержащейся в файле static/main/img/sprite.svg. Также это поле используется в качестве слага при указании на URL страницу', max_length=25, unique=True, verbose_name='URL адрес | Название иконки')),
            ],
            options={
                'verbose_name': 'Возможность сайта',
                'verbose_name_plural': 'Возможности сайта',
                'ordering': ['id'],
            },
        ),
    ]
