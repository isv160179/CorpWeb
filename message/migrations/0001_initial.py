# Generated by Django 4.0.6 on 2022-07-14 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140, verbose_name='Тема')),
                ('body', models.TextField(verbose_name='Сообщение')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Время отправления')),
                ('read_at', models.DateTimeField(blank=True, null=True, verbose_name='Время прочтения')),
                ('replied_at', models.DateTimeField(blank=True, null=True, verbose_name='Время ответа')),
                ('sender_deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления отправителем')),
                ('recipient_deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления получателем')),
                ('parent_msg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_messages', to='message.message', verbose_name='Родительское сообщение')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-sent_at'],
            },
        ),
    ]