from django import template


from news.models import NewsLikes, NewsComments

# Создаем экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
from users.models import Users

register = template.Library()



# @register.simple_tag()
# def add_like(user, news):
#     """
#     Функция получает на вход текущего пользователя, который ставит лайк
#     и добавляет новую запись в таблицу NewsLike
#     """
#     like = NewsLikes.objects.filter(news_id=news, author_id=user)
#     if like:
#         return 'Вы уже лайкали эту новость!'
#
#     NewsLikes.objects.create(author_id=user, news_id=news)
#     return 'Вы лайкнули сейчас эту новость!'


