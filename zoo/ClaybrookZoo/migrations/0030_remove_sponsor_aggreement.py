# Generated by Django 2.2.4 on 2020-03-30 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0029_booking_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='aggreement',
        ),
    ]
