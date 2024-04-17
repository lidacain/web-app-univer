# Generated by Django 4.2.7 on 2023-11-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_publishers_alter_table_options_alter_table_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='checks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('reader_id', models.IntegerField(verbose_name='Id читателя')),
                ('book_id', models.IntegerField(verbose_name='Id книги')),
                ('date', models.DateField(verbose_name='Дата выдачи')),
                ('return_date', models.DateField(verbose_name='Дата возврата')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
            },
        ),
        migrations.CreateModel(
            name='readers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
    ]