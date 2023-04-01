from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from home.models import WebsiteFeatures
from users.models import Users


class DataMixin(LoginRequiredMixin):
    """
    Класс наследуется от класса, который проверяет авторизирован ли пользователь.
    Если пользователь не авторизован, то доступ к страницам сайта будет запрещен.
    Так же класс предназначен для передачи контекста, который собирается из разных моделей.
    Данный класс используется в качестве родительского для классов-представлений.
    """
    login_url = reverse_lazy('home')  # Указываем страницу для входа в случае отсутствия авторизации
    raise_exception = True  # Генерация страницы 403 Доступ запрещен в случае неавторизованного пользователя

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = WebsiteFeatures.objects.filter(is_active=True)
        # context['user'] = Users.objects.all()
        if 'menu_selected' not in context:
            context['menu_selected'] = 0
        return context
