from django import forms
from django.contrib.auth.models import User
from .models import Negocio
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirma la contraseña')

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class NegocioForm(forms.ModelForm):
    class Meta:
        model = Negocio
        fields = ['nombre', 'rut', 'phone', 'newsletter', 'creation_date', 'num_employees']