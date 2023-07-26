from django.shortcuts import render
from django.http import HttpResponseNotFound , HttpResponseRedirect

path_list = {
    'home' : 'main/home.html',
    'cabinet' : 'main/cabinet.html',
    'works' : 'main/works.html',
    'examination' : 'main/examination.html',
    'feedback' : 'main/feedback.html',
    'about' : 'main/about.html',
             }


def get_page(request, page):

    path_way = path_list.get(page, None)

    combined_list = [('Главная страница' , 'home'),
                     ('Личный кабинет' , 'cabinet'),
                     ('Работы' , 'works'),
                     ('Тесты' , 'examination'),
                    ('Обратная связь' , 'feedback'),
                    ('О нас' , 'about')]
    paths_name = list(path_list)

    context = {
        'combined_list': combined_list,
        'paths_name': paths_name,
        }

    if path_way:
        return render(request, path_way, context=context)
    else:
        return HttpResponseNotFound('Данная страница не найдена')

def path_home(request):
    return HttpResponseRedirect('/home', get_page)