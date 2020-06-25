from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import (
    SignUpForm, SubmittableAuthenticationForm, SubmittablePasswordChangeForm
)
from hollymovies.mixins import TitleMixin


class SubmittableLoginView(TitleMixin, LoginView):
    title = 'Login'
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'


class SubmittablePasswordChangeView(TitleMixin, PasswordChangeView):
    title = 'Password Change'
    form_class = SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class SignUpView(TitleMixin, CreateView):
    title = 'Sign Up'
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')