from django import forms
from .models import Service 
from django.contrib.auth.models import User

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = '__all__'


class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']

		widgets = {
			"password" : forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())