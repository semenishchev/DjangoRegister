from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	field_order = ['username', 'email', 'password1', 'password2']