# Generated by Django 2.1.3 on 2018-12-09 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181209_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='client',
        ),
    ]
