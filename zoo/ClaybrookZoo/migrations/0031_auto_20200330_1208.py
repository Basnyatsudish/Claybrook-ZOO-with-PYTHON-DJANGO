# Generated by Django 2.2.4 on 2020-03-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0030_remove_sponsor_aggreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='primary_contact',
            field=models.FloatField(),
        ),
    ]
