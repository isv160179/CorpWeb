from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'sender', 'recipient', 'parent_msg', 'sent_at', 'read_at',
                    'replied_at', 'sender_deleted_at', 'recipient_deleted_at')  # Отображаемые поля
    list_display_links = ('subject',)  # Кликабельные поля


admin.site.register(Message, MessageAdmin)
