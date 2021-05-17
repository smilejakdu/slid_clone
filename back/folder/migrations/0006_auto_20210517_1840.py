# Generated by Django 3.1.5 on 2021-05-17 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0005_auto_20210517_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='depth_idx',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_folders', to='folder.folder'),
        ),
    ]
