# Generated by Django 4.0.6 on 2022-07-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_need_change_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='need_change_password',
        ),
    ]
