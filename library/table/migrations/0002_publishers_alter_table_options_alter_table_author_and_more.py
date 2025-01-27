# Generated by Django 4.2.7 on 2023-11-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='table',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='table',
            name='genre',
            field=models.CharField(max_length=100, verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='table',
            name='isbn',
            field=models.CharField(max_length=100, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='table',
            name='language',
            field=models.CharField(max_length=100, verbose_name='Язык книги'),
        ),
        migrations.AlterField(
            model_name='table',
            name='pages',
            field=models.IntegerField(verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='table',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='table',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='table',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='table',
            name='year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
    ]
