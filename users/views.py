from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'registration/login.html'



class ConfirmLogoutView(TemplateView):
    template_name = 'registration/logout_confirmation.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login'))  # Redirect to login page after logout

