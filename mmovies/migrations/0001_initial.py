# Generated by Django 3.1.2 on 2020-11-17 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_watchlist_parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_watchlist_child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchcheck', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mmovies.user_watchlist_parent')),
            ],
        ),
        migrations.CreateModel(
            name='all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('rate', models.FloatField(null=True)),
                ('story', models.TextField(null=True)),
                ('trailer', models.URLField(null=True)),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('series', 'Series')], max_length=100, null=True)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mmovies.sections')),
            ],
        ),
        migrations.CreateModel(
            name='actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('wikilink', models.URLField(null=True)),
                ('roles', models.ManyToManyField(to='mmovies.all')),
            ],
        ),
    ]
