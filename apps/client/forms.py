
from django import forms

# models
from django.contrib.auth.models import User


class ClientLoginForm(forms.Form):
    """ Formulario para el registro de usuario """
    model = User
    fields = ('username', 'password1', 'password2')
    widgets = {
        'username': forms.TextInput(attrs={'required': True}),
        'password1': forms.HiddenInput(attrs={'required': True}),
        'password2': forms.HiddenInput(attrs={'required': True}),
    }
    labels = {
        'username': 'Nombre de usuario*',
        'password1': 'Contraseña',
        'password2': 'Confirmar contraseña',
    }

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            return password2
