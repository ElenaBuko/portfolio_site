from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from apps.custom_auth.forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import UserCreationForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:index')


class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/blog/')

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def is_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:index')


    # def is_valid(self, form):
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
    #     password2 = form.cleaned_data.get('password2')

