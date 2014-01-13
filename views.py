from django.views.generic import DetailView, TemplateView
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect

from registration.backends.simple.views import RegistrationView
from registration import signals

from forms import Registration, JDUAuthenticationForm


class UserProfile(DetailView):
    template_name = 'justdifferentusers/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class Logout(TemplateView):
    """
    Logs out, redirects to login and applies appropriate message
    Very similar to django.contrib.auth.views logout_then_login or logout
    but cbv and more flexibility over message and more explicit
    """
    already_authed = "You have been successfully logged out"
    not_already_authed = "You weren't logged in!"

    template_name = 'justdifferentusers/generic.html'

    def get_message(self):
        return self.already_authed if self.request.user.is_authenticated() else self.not_already_authed

    def get_context_data(self, **kwargs):
        context = super(Logout, self).get_context_data(**kwargs)
        message = self.get_message()
        auth_logout(self.request)
        addition = {
            'title': 'Logged out',
            'message':message,
            'form': JDUAuthenticationForm,
            }
        context.update(addition)
        return context

    def dispatch(self, request, *args, **kwargs):
        return redirect(settings.LOGIN_URL, request)

class Registration(RegistrationView):
    template_name='justdifferentusers/generic.html'
    form_class = Registration
    success_url = '/auth/user'

    def get_success_url(self, request, user):
        #override to use success_url
        return (self.success_url, (), {})

    def register(self, request, **cleaned_data):
        """
        Copypasta from registration.backends.simple.views.RegistrationView
        Only change is to use get_user_model instead of
        django.contrib.auth.models.User !
        """
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        get_user_model().objects.create_user(username, email, password)

        new_user = authenticate(username=username, password=password)
        auth_login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)

    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:

            return self.form_invalid(form)



