from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm
from captcha.fields import CaptchaField

from .models import Departments, JobTitles


class UserLogin(AuthenticationForm):
    """ Форма аутентификации пользователя, которая используется на странице сайта"""
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'E-mail',
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form_input form_password',
            'placeholder': 'Введите пароль',
        }))
    captcha = CaptchaField()


class PasswordReset(PasswordResetForm):
    """ Форма сброса пароля пользователя с отправкой сообщения на почту, которая используется на странице сайта"""
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'E-mail'
        }))
    captcha = CaptchaField()


class SetPassword(SetPasswordForm):
    """ Форма установки нового пароля пользователя после сброса, которая используется на странице сайта"""
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'new-password',
            'class': 'form_input form_password',
            'placeholder': 'Новый пароль'
        }),

        strip=False, help_text=password_validation.password_validators_help_text_html(), )
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'new-password',
            'class': 'form_input form_password',
            'placeholder': 'Повторите пароль'}),
        strip=False, )


class AddUser(forms.Form):
    """ Форма добавление нового пользователя, которая используется на странице сайта. Используется форма не связанная
    с моделю User, так как при регистрации нового пользователя происходит генерация пароля случайным образом,
    и на почту нового пользователя приходит информация об учетных данных (логин, пароль) """
    name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'Имя'
        }))
    surname = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'Фамилия'
        }))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'E-mail'
        }))
    department = forms.ModelChoiceField(queryset=Departments.objects.all(), empty_label='Подразделение',
                                        widget=forms.Select(
                                            attrs={
                                                'class': 'form_input form_select',
                                            }))
    job_title = forms.ModelChoiceField(queryset=JobTitles.objects.all(), empty_label='Должность', widget=forms.Select(
        attrs={
            'class': 'form_input form_select',
        }))
    is_manager = forms.BooleanField(required=False,
                                    label='Руководитель',
                                    help_text='Сотрудник сможет заводить новых сотрудников в системе, удалять их из '
                                              'системы, направлять на курсы повышения квалификации')

    is_hr = forms.BooleanField(required=False,
                               label='Кадровый работник',
                               help_text='Нужен хотя-бы один кадровый работник в каждом подразделении, который будет '
                                         'иметь возможность проверять документы остальных сотрудников на правильность '
                                         'заполнения')

# class UserRegister(UserCreationForm):
#
#     def __init__(self, *args, **kwargs):  # Конструктор экземпляра класса UserRegister
#         super().__init__(*args, **kwargs)  # Вызываем конструктор базового класса UserCreationForm
#         self.fields['department'].empty_label = 'Укажите подразделение'
#         self.fields['job_title'].empty_label = 'Укажите должность'
#
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
#         attrs={
#             'class': 'form_input form_password',
#             'placeholder': 'Введите пароль',
#             'autocomplete': 'new-password', }),
#                                 help_text=password_validation.password_validators_help_text_html(), )
#
#     password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
#         attrs={
#             'class': 'form_input form_password',
#             'placeholder': 'Повторите пароль',
#             'autocomplete': 'new-password', }), )
#
#     class Meta:
#         model = Users
#         fields = ('name', 'surname', 'email', 'department', 'job_title', 'is_manager', 'is_hr')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'register-form_input', 'placeholder': 'Имя'}),
#             'surname': forms.TextInput(attrs={'class': 'register-form_input', 'placeholder': 'Фамилия'}),
#             'email': forms.EmailInput(attrs={'class': 'register-form_input', 'placeholder': 'E-mail'}),
#             'department': forms.Select(attrs={'class': 'register-form_input register-form_select'}),
#             'job_title': forms.Select(attrs={'class': 'register-form_input register-form_select'}),
#         }
#
#
# class UserChange(UserChangeForm):
#     class Meta:
#         model = Users
#         fields = ('name', 'surname', 'email',)
