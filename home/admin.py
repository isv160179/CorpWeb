from django.contrib import admin
from django.utils.safestring import mark_safe

from home.models import WebsiteFeatures


class WebsiteFeaturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'get_image', 'is_active', 'slug')  # Отображаемые поля
    list_display_links = ('title',)  # Кликабельные поля
    search_fields = ('title', 'content')  # Поля, по которым возможен поиск
    list_editable = ('is_active',)  # Редактируемые поля
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=70>")

    get_image.short_description = 'Миниатюра'


admin.site.register(WebsiteFeatures, WebsiteFeaturesAdmin)
