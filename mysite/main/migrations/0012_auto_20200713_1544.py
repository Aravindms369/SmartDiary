# Generated by Django 3.0.4 on 2020-07-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200713_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='color',
        ),
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]