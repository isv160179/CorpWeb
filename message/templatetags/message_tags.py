from django import template
from message.models import Message

register = template.Library()


@register.inclusion_tag('message/message.html')
def show_messages(user):
    """
        Функция возвращает все записи cо свойствами Видимый и Непрочитанный из модели Message,
        а так же количество этих записей
    """
    messages = Message.objects.filter(recipient=user, read_at__isnull=True,
                                      recipient_deleted_at__isnull=True).select_related('sender')
    return {'messages': messages, 'messages_count': messages.count()}
