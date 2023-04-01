from django.shortcuts import render

from home.models import WebsiteFeatures


def index(request):
    # Все записи из модели о возможностях сайта
    slides = WebsiteFeatures.objects.filter(is_active=True)

    return render(request, 'home/index.html',
                  {
                      'whatsapp_link': 'whatsapp://send?phone=<Указать номер телефона пользователя>&text=Мне%20нужна%20помощь%20на%20корпоративном%20сайте!',
                      'telegram_link': 'tg://resolve?domain=<Указать никнейм пользователя>',
                      'vk_link': 'https://vk.com/id1',
                      'title': 'Ваша безопасность',
                      'slides': slides,
                      'page': 'home',
                  })
