from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy,reverse

from users.forms import UserRegisterForm,UserProfileForm
from django.views.generic import CreateView,UpdateView, ListView, DetailView ,DeleteView
from users.models import User

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
import random

import secrets


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        token = secrets.token_hex(8)
        new_user.token = token
        new_user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/confirm/{token}'
        send_mail(
            subject="Подтверждение регистрации",
            message=f'Перейдите по ссылке для подтверждение регистрации {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def email_verification(request,token):
    new_user = get_object_or_404(User,token=token)
    new_user.is_active = True
    new_user.save()
    return redirect(reverse_lazy('users:login'))


class ProfileView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('medical_site:home')

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль : {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )
        request.user.set_password(new_password)
        request.user.save()
        return redirect(reverse('medical_site:home'))


class UserListView(ListView):
    model = User

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args,**kwargs)
        context_data['users_list'] = User.objects.all()
        return context_data

class UserDetailView(LoginRequiredMixin,DetailView):
    model = User

class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    login_url = 'users:login'
    success_url = reverse_lazy('users:user_list')

    def test_func(self):
        return self.request.user.is_staff
