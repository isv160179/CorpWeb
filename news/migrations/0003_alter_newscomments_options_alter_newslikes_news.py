# Generated by Django 4.0.6 on 2022-07-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscomments',
            options={'ordering': ['news_id', '-time_create'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='newslikes',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_likes', to='news.news', verbose_name='Понравившаяся новость'),
        ),
    ]
