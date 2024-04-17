from django.db import models


class Table(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=100)
    year = models.IntegerField('Год издания')
    pages = models.IntegerField('Количество страниц')
    genre = models.CharField('Жанр книги', max_length=100)
    language = models.CharField('Язык книги', max_length=100)
    publisher = models.CharField('Издательство', max_length=100)
    isbn = models.CharField('ISBN', max_length=100)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Publishers(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Название', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    email = models.CharField('Почта', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Readers(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    email = models.CharField('Почта', max_length=100)
    address = models.CharField('Адрес', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


class Checks(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    reader_id = models.IntegerField('Id читателя')
    book_id = models.IntegerField('Id книги')
    date = models.DateField('Дата выдачи')
    return_date = models.DateField('Дата возврата')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'


class Faculties(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Название', max_length=100)
    dean = models.CharField('Декан', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Departments(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Название', max_length=100)
    manager = models.CharField('Заведующий', max_length=100)
    faculty_id = models.IntegerField('Id факультета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Specialities(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Название', max_length=100)
    faculty_id = models.IntegerField('Id факультета')
    department_id = models.IntegerField('Id кафедры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Groups(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Название', max_length=100)
    course = models.IntegerField('Курс')
    language = models.CharField('Язык обучения', max_length=100)
    speciality_id = models.IntegerField('Id специальности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Students(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    email = models.CharField('Почта', max_length=100)
    phone_number = models.CharField('Телефон', max_length=100)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=100)
    group_id = models.IntegerField('Id группы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teachers(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    email = models.CharField('Почта', max_length=100)
    phone_number = models.CharField('Телефон', max_length=100)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=100)
    salary = models.IntegerField('Зарплата')
    department_id = models.IntegerField('Id кафедры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
