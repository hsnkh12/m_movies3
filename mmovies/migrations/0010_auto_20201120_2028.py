# Generated by Django 3.1.2 on 2020-11-20 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmovies', '0009_user_watchlist_child_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_watchlist_child',
            old_name='data',
            new_name='d',
        ),
    ]
