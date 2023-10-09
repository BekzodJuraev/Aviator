from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,label="Логин")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput,label="Пароль")

CURRENCY_CHOICES = [
    ('KZT', 'Казахстанский тенге(KZT)'),
    ('RUB', 'Российский рубль(RUB)'),
    ('UZS', 'Узбекистанский сум(UZS)'),

]

class RegistrationForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label='Выберите валюту')
    username = forms.CharField(max_length=63, label='Придумайте логин')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Придумайте пароль')
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Повторите Пароль')
    email = forms.EmailField(label='Ввидите E-mail (необязательно)',required=False )

    class Meta:
        model=User
        fields=['currency','username','password','password2','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


