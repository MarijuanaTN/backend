# Generated by Django 3.2.18 on 2023-04-27 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monthly', '0002_auto_20230427_1412'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ForexData_Weekly',
            new_name='ForexData_Monthly',
        ),
    ]