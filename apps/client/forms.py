
from django import forms

# models
from django.contrib.auth.models import User


class ClientLoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario*",
                               widget=forms.TextInput(attrs={'required': True, 'class': 'field-account'}))
    password = forms.CharField(label="Contraseña*",
                               widget=forms.PasswordInput(attrs={'required': True, 'class': 'field-account'}))


class ClientSignUpForm(forms.Form):
    """ Formulario para el registro de usuario """
    username = forms.CharField(label='Nombre de usuario*', min_length=4, max_length=150,
                               widget=forms.TextInput(attrs={'required': True, 'class': 'field-account'}))
    email = forms.EmailField(label='Correo electronico*',
                             widget=forms.TextInput(attrs={'required': True, 'class': 'field-account'}))
    password1 = forms.CharField(label='Contraseña*',
                                widget=forms.PasswordInput(attrs={'required': True, 'class': 'field-account'}))
    password2 = forms.CharField(label='Confirme su Contraseña*',
                                widget=forms.PasswordInput(attrs={'required': True, 'class': 'field-account'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        user = User.objects.filter(username=username)
        if user.count():
            raise forms.ValidationError("El usuario ya existe")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
