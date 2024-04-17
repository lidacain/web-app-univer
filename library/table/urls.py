from django.urls import path
from . import views


urlpatterns = [
    path('faculties/', views.data, name='faculties'),
    path('departments/', views.departments, name='departments'),
    path('specialties/', views.specialties, name='specialties'),
    path('groups/', views.groups, name='groups'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),

    path('form/', views.form_faculties, name='form'),
    path('form/data/', views.form_faculties, name='form_faculties'),
    path('form/departments/', views.form_departments, name='form_departments'),
    path('form/specialities/', views.form_specialities, name='form_specialities'),
    path('form/groups/', views.form_groups, name='form_groups'),
    path('form/students/', views.form_students, name='form_students'),
    path('form/teachers/', views.form_teachers, name='form_teachers'),
]

