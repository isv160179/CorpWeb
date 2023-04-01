from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from users.models import Users, Departments, Avatars, JobTitles


class UsersAdmin(UserAdmin):
    """
    Класс содержит аргументы, которые будут влиять на
    форму отображения таблицы в админ-панели
    """
    model = Users

    list_display = ('email', 'name', 'patronymic', 'surname', 'get_image')
    list_filter = ('is_active', 'department', 'job_title', 'is_manager', 'is_hr',)

    fieldsets = (
        (None, {'fields': (
            'name',
            'surname',
            'patronymic',
            'department',
            'job_title',
            'phone',
            'date_of_birth',
            'avatar',
            'get_image',
            'email',
            'password',
            'date_joined',
        )}),
        ('Разрешения', {'fields': (
            'is_staff',
            'is_active',
            'is_manager',
            'is_hr',
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'surname',
                'department',
                'job_title',
                'email',
                'password1',
                'password2',
            )}),
        ('Разрешения', {'fields': (
            'is_manager',
            'is_hr',
            'is_staff',
            'is_superuser',
        )}),
    )
    readonly_fields = ('date_joined', 'get_image',)
    search_fields = ('email', 'name', 'surname', 'department', 'job_title',)
    ordering = ('surname', 'name', 'email',)

    def get_image(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.avatar.url}' width=50>")

    get_image.short_description = 'Миниатюра'


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'department',)
    list_display_links = ('department',)


class AvatarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image',)
    list_display_links = ('id',)

    def get_image(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_image.short_description = 'Миниатюра'


class JobTitlesAdmin(admin.ModelAdmin):
    list_display = ('job_title',)
    list_display_links = ('job_title',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Avatars, AvatarsAdmin)
admin.site.register(JobTitles, JobTitlesAdmin)
