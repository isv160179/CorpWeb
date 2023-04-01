from django.http import HttpResponseNotFound


def pageNotFound(request, exception):
    """ Функция отлавливает исключения несуществующей страницы """
    return HttpResponseNotFound('<h1>Увы, такой страницы нет на нашем сайте!</h>')
