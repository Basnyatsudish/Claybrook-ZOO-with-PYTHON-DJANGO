# Generated by Django 2.2.4 on 2020-04-07 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0047_message_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
