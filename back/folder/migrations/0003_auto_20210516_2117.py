# Generated by Django 3.1.5 on 2021-05-16 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0002_auto_20210516_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='folder_name',
            new_name='name',
        ),
    ]
