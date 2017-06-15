import re
import random

from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Person


def index(request):
    return render(request, 'random_winners/index.html')


def add_person(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get('name')

        if not name:
            return JsonResponse({"success": "Пожалуйста, введите имя пользователя"})
        elif re.fullmatch('^[А-Яа-яA-Za-z]+$', name) is None:
            return JsonResponse({"success": "Используйте в имени только буквы, логично не правда ли?"})

        name = name.lower().capitalize()

        if Person.objects.filter(name=name).exists():
            return JsonResponse({"success": "Имя {} уже существует в базе".format(name)})
        else:
            Person.objects.create(name=name)
            return JsonResponse({"success": "Имя {} успешно добавлено!".format(name)})


def delete_person(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get('name')

        if not name:
            return JsonResponse({"success": "Пожалуйста, введите имя пользователя"})
        elif re.fullmatch('^[А-Яа-яA-Za-z]+$', name) is None:
            return JsonResponse({"success": "Используйте в имени только буквы, логично не правда ли?"})

        name = name.lower().capitalize()

        if Person.objects.filter(name=name).exists():
            Person.objects.get(name=name).delete()
            return JsonResponse({"success": "Имя {} успешно удалено из базы".format(name)})
        else:
            return JsonResponse({"success": "Имени {} не существует в базе".format(name)})


def call_three_random_names(request):
    if request.method == 'POST' and request.is_ajax():
        return JsonResponse({"success": "И вот наши счастливчики! {}".format(', '.join(get_three_random_names()))})
    else:
        return JsonResponse({"success": "Неправильно отправлен запрос. Пожалуйста попробуйте еще раз"})


def get_three_random_names():
    persons_count = Person.objects.all().count()

    if persons_count <= 3:
        random_values = random.sample(range(persons_count), persons_count)
    else:
        random_values = random.sample(range(persons_count), 3)
    persons = Person.objects.all()

    return [persons[value].name for value in random_values]
