# Generated by Django 4.0.6 on 2022-07-15 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_users_need_change_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.departments', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пользователь базы данных'),
        ),
        migrations.AlterField(
            model_name='users',
            name='job_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.jobtitles', verbose_name='Должность'),
        ),
    ]
