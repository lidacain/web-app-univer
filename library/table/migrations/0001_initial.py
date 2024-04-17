# Generated by Django 4.2.7 on 2023-11-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
