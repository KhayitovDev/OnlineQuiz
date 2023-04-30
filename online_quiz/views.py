from django.shortcuts import render
from .models import User, Category
from django.views.generic import ListView
from django.views.generic.edit import CreateView
import random
# Create your views here.



class CreateUser(CreateView):
    model=User
    fields='__all__'
    template_name='folder/login.html'
    success_url='category'


class CategoryView(ListView):
    model=Category
    template_name='folder/main.html'
    success_url='quiz'

def category(request):
    category_view=Category.objects.all()
    context={'category_view':category_view}
    return render(request, 'folder/main.html', context)

