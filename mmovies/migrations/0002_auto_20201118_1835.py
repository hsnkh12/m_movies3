# Generated by Django 3.1.2 on 2020-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmovies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='wikilink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='all',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]
