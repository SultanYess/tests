from .models import Pets
from django.forms import CharField, Textarea, ModelForm, TextInput

class PetsForm(ModelForm):
    class Meta:
        model = Pets
        fields = "__all__"

        widgets = {
            "pets_name":TextInput(attrs={
                "class": "form-control",
                'placeholder': "Имя питомца"
            }),
            "content":Textarea(attrs={
                "class": "form-control",
                "placeholder": "Контент",
            })
        }