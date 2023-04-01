from django import template


from news.models import NewsLikes, NewsComments



# Создаем экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
from users.models import Users

register = template.Library()


@register.simple_tag()
def choose_plural(amount: int, declensions: tuple) -> str:
    """
    Функция принимает целое число (int) и существительное в трех формах (tuple):
    1. именительный падеж единственное число,
    2. родительный падеж единственное число,
    3. родительный падеж множественное число
    например: ('пример', 'примера', 'примеров') и
    возвращает существительное в той форме, которая согласуется с полученным числом.
    """
    if amount % 10 in range(2, 5) and amount % 100 not in range(12,15):
        return declensions[1]
    if amount % 10 == 1 and amount % 100 != 11:
        return declensions[0]
    return declensions[2]

@register.simple_tag
def update_variable(value, delta):
    value += delta
    return value
