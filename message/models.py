from django.db import models
from django.urls import reverse
from django.utils import timezone

from CorpWebsite import settings


class MessageManager(models.Manager):

    def inbox_for(self, user):
        """
        Возвращает все сообщения, которые были получены данным пользователем и не
        отмечены как удаленные.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=True,
        )

    def outbox_for(self, user):
        """
        Возвращает все сообщения, которые были отправлены данным пользователем и не
        отмечены как удаленные.
        """
        return self.filter(
            sender=user,
            sender_deleted_at__isnull=True,
        )

    def trash_for(self, user):
        """
        Возвращает все сообщения, которые были получены или отправлены данным
        пользователя и помечены как удаленные.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=False,
        ) | self.filter(
            sender=user,
            sender_deleted_at__isnull=False,
        )


class Message(models.Model):
    """
    Личные сообщения от пользователя к пользователю
    """
    subject = models.CharField('Тема', max_length=140)
    body = models.TextField('Сообщение')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', verbose_name='Отправитель',
                               on_delete=models.PROTECT)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', null=True, blank=True,
                                  verbose_name='Получатель', on_delete=models.SET_NULL)
    parent_msg = models.ForeignKey('self', related_name='next_messages', null=True, blank=True,
                                   verbose_name='Родительское сообщение', on_delete=models.SET_NULL)
    sent_at = models.DateTimeField('Время отправления', null=True, blank=True)
    read_at = models.DateTimeField('Время прочтения', null=True, blank=True)
    replied_at = models.DateTimeField('Время ответа', null=True, blank=True)
    sender_deleted_at = models.DateTimeField('Время удаления отправителем', null=True, blank=True)
    recipient_deleted_at = models.DateTimeField('Время удаления получателем', null=True, blank=True)

    objects = MessageManager()

    def new(self):
        """ Возвращает, прочитал ли получатель сообщение или нет """
        if self.read_at is not None:
            return False
        return True

    def replied(self):
        """ Возвращает, написал ли получатель ответ на это сообщение """
        if self.replied_at is not None:
            return True
        return False

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('messages_detail', args=[self.id])

    def save(self, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


# def inbox_count_for(user):
#     """
#     Возвращает количество непрочитанных сообщений для данного пользователя, но не помечает их как просмотренные
#     """
#     return Message.objects.filter(recipient=user, read_at__isnull=True, recipient_deleted_at__isnull=True).count()
