# Generated by Django 3.0.7 on 2021-05-15 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contents', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trash_bool', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder.Folder')),
            ],
            options={
                'db_table': 'boards',
            },
        ),
    ]
