from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from registration.forms import RegistrationFormUniqueEmail

from models import IQUser


User = get_user_model()

class DjangoRegistrationFixin(object):

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

class Registration(DjangoRegistrationFixin, RegistrationFormUniqueEmail):
    action_name = 'Register'

class JDUAuthenticationForm(AuthenticationForm):
    action_name = 'Login'