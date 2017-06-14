from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        labels = {
            "name": "Введите имя:"
        }
        fields = "__all__"
