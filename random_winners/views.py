import random

from django.http.response import JsonResponse
from django.shortcuts import render

from .forms import PersonForm
from .models import Person


# Create your views here.
def send_form(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].lower()
            name = name.capitalize()
            if Person.objects.filter(name=name).exists():
                return JsonResponse("Name {} is exist in DB".format(name), safe=False)
            else:
                person = form.save(commit=False)
                person.name = name
                person.save()
            return JsonResponse("Name {} is successfully added!".format(person.name), safe=False)
    else:
        form = PersonForm()
    return render(request, "random_winners/index.html", {'form': form})


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