from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterForm(forms.Form):
    WORK_CHOICES = [
        ('employed', 'employed'),
        ('unemployed', 'unemployed'),
        ('student', 'student'),
    ]
    HOBBY_CHOICES = [
        ('games', 'games'),
        ('sports', 'sports'),
        ('food', 'food'),
        ('dances', 'dances'),
    ]

    name = forms.CharField(max_length=100, label="Name")
    login = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    age = forms.IntegerField(min_value=1, max_value=101, label="Age")
    work = forms.ChoiceField(choices=WORK_CHOICES, label="Work")
    hobby = forms.MultipleChoiceField(
        choices=HOBBY_CHOICES,
        widget=forms.SelectMultiple,
        label="Hobby",
    )

    def clean_login(self):
        login = self.cleaned_data['login'].lower()
        if User.objects.filter(username=login).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return login

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)  # правила из AUTH_PASSWORD_VALIDATORS
        return password

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') and cleaned.get('confirm_password'):
            if cleaned['password'] != cleaned['confirm_password']:
                self.add_error('confirm_password', "Пароли не совпадают")
        return cleaned

