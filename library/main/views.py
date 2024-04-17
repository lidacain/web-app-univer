from django.shortcuts import render


def index(request):
    dic = {
        'title': 'UNIVERSITY DATABASE',
    }
    return render(request, 'main/index.html', dic)


def about(request):
    dic = {
        'title': 'Про базу данных',
    }
    return render(request, 'main/about.html', dic)


def data(request):
    dic = {
        'title': 'Таблицы',
    }
    return render(request, 'table/faculties.html', dic)



def author(request):
    dic = {
        'title': 'Об авторе',
    }
    return render(request, 'main/author.html', dic)

