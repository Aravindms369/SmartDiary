# Generated by Django 3.0.4 on 2020-07-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_post_public_or_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public_or_private',
            field=models.CharField(max_length=200),
        ),
    ]