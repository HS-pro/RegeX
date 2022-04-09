# Generated by Django 4.0.3 on 2022-04-09 10:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('link', models.URLField(unique=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), size=None)),
                ('image', models.URLField(unique=True)),
                ('publication_name', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='BlogLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_name', models.CharField(max_length=256)),
                ('rss_link', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(max_length=256, unique=True)),
                ('publication_logo', models.CharField(max_length=2048)),
                ('description', models.CharField(max_length=2048)),
                ('link', models.URLField(max_length=2048, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048, unique=True)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=2048)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('image', models.URLField(max_length=2048)),
                ('audio_link', models.URLField(max_length=2048)),
                ('publication_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fetcher.podlinks')),
            ],
        ),
    ]
