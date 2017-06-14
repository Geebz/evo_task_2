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
                form.save(commit=False)
                form.name = name
                form.save()
            return JsonResponse("Name {} is successfully added!".format(form.cleaned_data['name']), safe=False)
    else:
        form = PersonForm()
    return render(request, "random_winners/index.html", {'form': form})



