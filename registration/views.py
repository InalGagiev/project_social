from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registrations/login.html'

    def get_success_url(self):
        return reverse_lazy('list_records')

@login_required
def logout_user(request):
    logout(request)
    return redirect('list_records')

#функция регистрации
class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registrations/register.html'


#профиль
"""@login_requered служит для того чтобы не давать доступ не авторизованному пользователю а этой вьюшке"""
class UserProfile(LoginRequiredMixin, DetailView):
    model = Profile
    slug_field = 'id'
    template_name = 'registrations/profile.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))