# Generated by Django 4.0.6 on 2022-07-29 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigpotapp', '0002_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freepost',
            old_name='author',
            new_name='author_id',
        ),
    ]