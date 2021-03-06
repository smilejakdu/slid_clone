# Generated by Django 3.0.7 on 2021-05-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
