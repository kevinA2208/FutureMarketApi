# Generated by Django 3.2.1 on 2023-02-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlobalApi', '0007_auto_20230130_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_active',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
