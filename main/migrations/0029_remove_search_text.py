# Generated by Django 3.0.4 on 2020-07-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_post_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='text',
        ),
    ]
