from .models import Table, Publishers, Readers, Checks
from django.forms import ModelForm, TextInput, DateInput, NumberInput
from .models import Faculties, Departments, Specialities, Groups, Students, Teachers


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['id', 'title', 'author', 'year', 'pages', 'genre', 'language', 'publisher', 'isbn', 'price']

        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
            "year": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год издания'
            }),
            "pages": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество страниц'
            }),
            "genre": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите жанр книги'
            }),
            "language": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите язык книги'
            }),
            "publisher": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название издательства'
            }),
            "isbn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ISBN'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
        }


class PublisherForm(ModelForm):
    class Meta:
        model = Publishers
        fields = ['id', 'name', 'address', 'phone', 'email']

        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
        }


class ReadersForm(ModelForm):
    class Meta:
        model = Readers
        fields = ['id', 'name', 'surname', 'phone', 'email', 'address']

        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
        }


class DateInput(DateInput):
    input_type = 'date'


class ChecksForm(ModelForm):
    class Meta:
        model = Checks
        fields = ['id', 'reader_id', 'book_id', 'date', 'return_date']

        widgets = {
            "id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id'
            }),
            "reader_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id читателя'
            }),
            "book_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id книги'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату выдачи'
            }),
            "return_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату возврата'
            }),
        }


class FacultiesForm(ModelForm):
    class Meta:
        model = Faculties
        fields = ['name', 'dean']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "dean": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите декана'
            }),
        }


class DepartmentsForm(ModelForm):
    class Meta:
        model = Departments
        fields = ['name', 'manager', 'faculty_id']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "manager": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заведующего'
            }),
            "faculty_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id факультета'
            }),
        }


class SpecialitiesForm(ModelForm):
    class Meta:
        model = Specialities
        fields = ['name', 'faculty_id', 'department_id']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "faculty_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id факультета'
            }),
            "department_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id кафедры'
            }),
        }


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'course', 'language', 'speciality_id']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "course": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите курс'
            }),
            "language": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите язык обучения'
            }),
            "speciality_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id специальности'
            }),
        }


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'surname', 'email', 'phone_number', 'date_of_birth', 'address', 'group_id']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "group_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id группы'
            }),
        }


class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['name', 'surname', 'email', 'phone_number', 'date_of_birth', 'address', 'salary', 'department_id']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "salary": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите зарплату'
            }),
            "department_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id кафедры'
            }),
        }