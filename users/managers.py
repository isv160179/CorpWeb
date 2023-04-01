from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail


from CorpWebsite import settings


class UserManager(BaseUserManager):
    """
    Менеджер модели Пользователя, который использует электронную почту
    в качестве уникального идентификатора вместо имени пользователя.
    После успешного добавления пользователя в базу данных на его
    электронную почту приходит письмо с логином и паролем.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создает и записывает пользователя с полученными электронной почтой
        и паролем из функции adduser в файле views.py
        """
        if not email:
            raise ValueError('Должен быть указан E-mail')
        email = self.normalize_email(email)

        if extra_fields.get('name'):
            name = extra_fields.get('name')
        else:
            name = 'Администратор'

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()


         # Формирование и отправка письма пользователю
        send_mail(
            'Учетная запись на корпоративном сайте Ваша Безопасность',
            'Добрый день, ' + name + '!\n'
            'Для вас создана учетная запись на корпоративном сайте со следующими данными:\n'
            'Логин : ' + email + '\n'
            'Пароль : ' + password + '\n'
            'В дальнейшем, при желании, Вы сможете изменить этот пароль в личном кабинете \n'
            'Начать работу на сайте Вы можете, перейдя по ссылке: ' + settings.SITE_NAME + '\n'
            'С уважением, команда сайта Ваша Безопасность.',
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и записывает суперпользователя с полученными электронной почтой и паролем
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('У суперпользователя атрибут "is_staff" должен быть True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('У суперпользователя атрибут "is_superuser" должен быть True.')
        return self.create_user(email, password, **extra_fields)

