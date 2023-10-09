from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView

User = get_user_model()

class UserRegisterView(CreateView):
    model = User
    fields = ['username', 'password', 'email', 'full_name', 'contact_number', 'bio']
    template_name = 'users/register.html'

class UserProfileView(UpdateView):
    model = User
    fields = ['username', 'email', 'full_name', 'contact_number', 'bio']
    template_name = 'users/profile.html'
