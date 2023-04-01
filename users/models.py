from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from users.managers import UserManager


class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', null=True, blank=True)
    job_title = models.ForeignKey('JobTitles', on_delete=models.PROTECT, related_name='users',
                                  verbose_name='Должность', null=True, blank=True)
    email = models.EmailField(max_length=150, verbose_name='E-mail', unique=True)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_regex], max_length=16, null=True, blank=True,
                             verbose_name='Номер телефона')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Пользователь базы данных', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    department = models.ForeignKey('Departments', on_delete=models.PROTECT, related_name='users',
                                   verbose_name='Подразделение', null=True, blank=True)
    avatar = models.ForeignKey('Avatars', on_delete=models.PROTECT, related_name='users',
                               verbose_name='Аватарка', null=True, blank=True)
    is_manager = models.BooleanField(default=False, verbose_name='Руководитель',
                                     help_text='Руководитель сможет заводить новых сотрудников в системе, удалять их из '
                                               'системы, направлять на курсы повышения квалификации')
    is_hr = models.BooleanField(default=False, verbose_name='Кадровый работник',
                                help_text='Нужен хотя-бы один кадровый работник в каждом подразделении, который будет '
                                          'иметь возможность проверять документы остальных сотрудников на '
                                          'правильность заполнения')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"


class Avatars(models.Model):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватарки', blank=True, null=True)

    def __str__(self):
        return self.avatar.url

    class Meta:
        verbose_name = "Аватарка"
        verbose_name_plural = "Аватарки"


class Departments(models.Model):
    department = models.CharField(max_length=150, verbose_name='Город', null=True, blank=True)

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"
        ordering = ['department']


class JobTitles(models.Model):
    job_title = models.CharField(max_length=150, verbose_name='Должность', null=True, blank=True)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ['job_title']
