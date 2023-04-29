from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView
# Create your views here.



class CreateUser(CreateView):
    model=User
    fields='__all__'
    template_name='folder/login.html'
    success_url='admin/online_quiz/user/'
