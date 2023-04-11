from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """Meta, нужен для того, чтобы добавить поля из модели в форму для заполнения"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



