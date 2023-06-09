# Generated by Django 4.0.6 on 2022-07-10 15:23

import django.core.validators
from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватарки')),
            ],
            options={
                'verbose_name': 'Аватарка',
                'verbose_name_plural': 'Аватарки',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=150, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='JobTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['job_title'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Пользователь базы данных')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_manager', models.BooleanField(default=False, help_text='Сотрудник сможет заводить новых сотрудников в системе, удалять их из системы, направлять на курсы повышения квалификации', verbose_name='Руководитель')),
                ('is_hr', models.BooleanField(default=False, help_text='Нужен хотя-бы один кадровый работник в каждом подразделении, который будет иметь возможность проверять документы остальных сотрудников на правильность заполнения', verbose_name='Кадровый работник')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Верифицированный')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
