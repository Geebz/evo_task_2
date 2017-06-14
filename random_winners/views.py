from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import PersonForm


# Create your views here.
def send_form(request):
    if request.method == "POST" and request.is_ajax():
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return JsonResponse({"Имя {} успешно добавлено!".format(form.cleaned_data['my_form_field_name'])})
    else:
        form = PersonForm()
    return render(request, "random_winners/index.html", {'form': form})

