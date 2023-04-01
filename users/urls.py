from django.urls import path

from users.views import *

urlpatterns = [
    path('', index, name='users'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('password_reset/', PasswordUserReset.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html", title='Проверьте почту'),
         name='password_reset_done'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html', title='Пароль изменен'),
         name='password_reset_complete'),
    path('add_user/', adduser, name='add_user'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('settings/', SettingsUserVB.as_view(), name='settings'),
    # path('password_change/', password_change, name='password_change'),
    # path('password_change_done/', password_change_done, name='password_change_done'),
]
