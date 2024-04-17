from django.shortcuts import render, redirect
from .forms import TableForm, ChecksForm, ReadersForm, PublisherForm
from .models import Faculties, Departments, Specialities, Groups, Students, Teachers
from .forms import FacultiesForm, DepartmentsForm, SpecialitiesForm, GroupsForm, StudentsForm, TeachersForm


def data(request):
    datas = Faculties.objects.order_by('id').all()
    return render(request, 'table/faculties.html', {'data': datas})


def departments(request):
    datas = Departments.objects.order_by('id').all()
    return render(request, 'table/departments.html', {'data': datas})


def specialties(request):
    datas = Specialities.objects.order_by('id').all()
    return render(request, 'table/specialties.html', {'data': datas})


def groups(request):
    datas = Groups.objects.order_by('id').all()
    return render(request, 'table/groups.html', {'data': datas})


def students(request):
    datas = Students.objects.order_by('id').all()
    return render(request, 'table/students.html', {'data': datas})


def teachers(request):
    datas = Teachers.objects.order_by('id').all()
    return render(request, 'table/teachers.html', {'data': datas})


def form_faculties(request):
    error = ''
    if request.method == 'POST':
        forma = FacultiesForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('faculties')
        else:
            error = 'Форма была неверной'
    forma = FacultiesForm()
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_faculties.html', datas)


def form_departments(request):
    error = ''
    if request.method == 'POST':
        forma = DepartmentsForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('departments')
        else:
            error = 'Форма была неверной'
    forma = DepartmentsForm()
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_departments.html', datas)


def form_specialities(request):
    error = ''
    if request.method == 'POST':
        forma = SpecialitiesForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('specialties')
        else:
            error = 'Форма была неверной'
    forma = SpecialitiesForm
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_specialities.html', datas)


def form_groups(request):
    error = ''
    if request.method == 'POST':
        forma = GroupsForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('groups')
        else:
            error = 'Форма была неверной'
    forma = GroupsForm
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_groups.html', datas)


def form_students(request):
    error = ''
    if request.method == 'POST':
        forma = StudentsForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('students')
        else:
            error = 'Форма была неверной'
    forma = StudentsForm
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_students.html', datas)


def form_teachers(request):
    error = ''
    if request.method == 'POST':
        forma = TeachersForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('teachers')
        else:
            error = 'Форма была неверной'
    forma = TeachersForm
    datas = {'form': forma, 'error': error}
    return render(request, 'table/form_teachers.html', datas)
