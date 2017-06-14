import re
import random

from django.http.response import JsonResponse
from django.shortcuts import render

from .forms import PersonForm
from .models import Person


# Create your views here.

def send_form_ajax(request):
    if request.method == "POST":
        Person.objects.create(name='test')
        name = request.POST.get('post_data')

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


def index(request):
    return render(request, 'random_winners/index.html')


def call_three_random_names(request):
    if request.method == 'POST':
        return ', '.join(get_three_random_names())
    else:
        return JsonResponse("Неправильно отправлен запрос. Пожалуйста попробуйте еще раз".format(), safe=False)


def get_three_random_names():
    persons_count = Person.objects.all().count()

    if persons_count <= 3:
        random_values = random.sample(range(persons_count), persons_count)
    else:
        random_values = random.sample(range(persons_count), 3)
    persons = Person.objects.all()

    return [persons[value].name for value in random_values]