# Generated by Django 3.0.4 on 2020-07-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200713_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]