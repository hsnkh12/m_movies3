# Generated by Django 3.1.2 on 2020-11-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmovies', '0004_auto_20201118_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all',
            old_name='fullname',
            new_name='name',
        ),
    ]