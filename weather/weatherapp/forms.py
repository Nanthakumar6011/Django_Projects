# from django.forms import ModelForm,TextInput
# from .models import City

# class CityForm(ModelForm):
#     class Meta:
#         model=City
#         fields=["name"]
#         widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City Name'})}\
from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name"]  # Field from the City model to be included in the form
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap class for styling
                'placeholder': 'City Name'  # Placeholder text
            })
        }
