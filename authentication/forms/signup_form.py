from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import User


class SignupForm(UserCreationForm):
    """
    Signum form with email, username, and 2 password fields.
    """
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username')
