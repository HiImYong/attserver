# Generated by Django 4.2.2 on 2023-06-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_lasttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lasttime',
            name='userIdx',
        ),
        migrations.AddField(
            model_name='lasttime',
            name='userId',
            field=models.CharField(default=1, max_length=30, unique=1),
            preserve_default=False,
        ),
    ]