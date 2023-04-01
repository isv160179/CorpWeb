from django.contrib.auth import logout
from django.contrib.auth.views import *
from django.shortcuts import render, redirect
from django.urls import reverse

from CorpWebsite.utils import DataMixin
from home.models import WebsiteFeatures
from users.forms import AddUser, UserLogin, PasswordReset, SetPassword
from users.models import Users


@login_required
def index(request):
    """ Информации по сотрудникам  - НУЖНО ПЕРЕДЕЛАТЬ НА КЛАСС ПРЕДСТАВЛЕНИЯ LISTVIEW"""
    context = {'title': 'Мои коллеги', 'menu_selected': 6,
               'menu': WebsiteFeatures.objects.filter(is_active=True)}
    return render(request, 'users/home.html', context)


@login_required
def adduser(request):
    """ Функция представления добавления нового пользователя """
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            try:
                password = Users.objects.make_random_password()
                Users.objects.create_user(password=password, **form.cleaned_data)
                return redirect('users')
            except:
                form.add_error(None, 'Пользователь с таким E-mail уже зарегистрирован')
    else:
        form = AddUser()

    context = {'title': 'Добавить сотрудника', 'menu_selected': 0,
               'menu': WebsiteFeatures.objects.filter(is_active=True),
               'form': form,
               }
    return render(request, 'users/add_user.html', context)


def logout_user(request):
    """ Функция представления выхода из учетной записи пользователя """
    logout(request)
    return redirect('home')


class LoginUser(LoginView):
    """ Класс представления авторизации пользователя"""
    template_name = 'users/login.html'
    form_class = UserLogin
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse('news')


class PasswordUserReset(PasswordResetView):
    """ Класс представления сброса пароля пользователя"""
    template_name = 'users/password_reset_form.html'
    title = "Восстановить пароль"
    form_class = PasswordReset


class PasswordResetConfirm(PasswordResetConfirmView):
    """ Класс представления задания нового пароля пользователя после сброса"""
    template_name = 'users/password_reset_confirm.html'
    title = "Новый пароль"
    form_class = SetPassword