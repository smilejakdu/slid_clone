# Generated by Django 3.0.7 on 2021-05-15 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_idx', models.CharField(max_length=100, null=True)),
                ('folder_name', models.CharField(max_length=100)),
                ('depth_idx', models.IntegerField(null=True)),
                ('trash_bool', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'folder',
            },
        ),
    ]
