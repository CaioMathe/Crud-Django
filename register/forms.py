from django import forms
from django.forms.widgets import NumberInput
from register.models import Cadas



class ClientForm(forms.ModelForm):
    class Meta:
        model = Cadas
        fields = ["nome", "sobrenome", "email", "data_nascimento", 'celular',"genero" , 'leg_prog', 'trabalhou','softskills']

        widgets ={
            'data_nascimento': NumberInput(attrs={'type': 'date'}),
            'leg_prog': forms.RadioSelect,
            'softskills': forms.Textarea({'rows': 5, 'cols': 70})
        }