# Generated by Django 3.0.4 on 2020-04-04 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_users_isdeleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='IsSuperUseer',
            new_name='IsSuperUser',
        ),
    ]
