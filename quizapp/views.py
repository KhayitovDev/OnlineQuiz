from typing import Any, Dict
from django.db import models
from random import shuffle
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView,CreateView
from .models import Quiz, Category, Level, UserAnswer
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomLoginForm, QuizCreationForm, CategoryCreationForm, LevelCreationForm
from django.contrib.auth.views import LoginView, LogoutView



class UserCreateView(CreateView):
    form_class=CustomUserCreationForm
    template_name='register.html'
    success_url=reverse_lazy('login')

class UserLogin(LoginView):
    form_class=CustomLoginForm
    template_name='login.html'
    success_url=reverse_lazy('category')

class UserLogout(LogoutView):
    next_page=reverse_lazy('category')

class CategoryListView(ListView):
    template_name='category.html'
    context_object_name='categories'
    queryset=Category.objects.all()
 
class LevelsListView(ListView):
    template_name='level.html'
    queryset=Level.objects.all()
    context_object_name='levels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Level.objects.filter(quiz__category_id=category_id).distinct()

class QuizListView(LoginRequiredMixin, ListView):
    template_name = 'quiz_page.html'
    context_object_name = 'quizzes'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        level_id = self.kwargs['pk']
        queryset=list(Quiz.objects.filter(category_id=category_id, levels_id=level_id))
        shuffle(queryset)
        return queryset
    
    def post(self, request, category_id, pk, *args, **kwargs):
        form_data = request.POST
        quizzes = self.get_queryset()
        form_data=request.POST
       

        score = 0
        correct = 0
        wrong = 0
        total=0

        for quiz in quizzes:
            total +=1
            submitted_answer = form_data.get(str(quiz.id))
            correct_answer = quiz.correct_answers
            if submitted_answer == correct_answer:
                score +=1
                correct +=1
            else:
                wrong +=1
        
        percentage = (score / total ) * 100
        #---------------------------------#
        user=request.user
        category = Category.objects.get(id=category_id)
        level = Level.objects.get(id=pk)
        UserAnswer.objects.create(user=user, category=category, level=level, score=score)

        #---------------------------------#
        result = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'correct': correct,
            'wrong': wrong,
            'user':user,
            'category_id': category_id,
            'pk': pk,
        }

        return render(request, 'result.html', {'result': result})

class LeadboardListView(LoginRequiredMixin, ListView):
    template_name = 'leaderboard.html'
    context_object_name = 'leaders'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        level_id = self.kwargs['pk']
        queryset = UserAnswer.objects.filter(category_id=category_id, level_id=level_id).order_by('-score')
        return queryset
    
class QuizCreateView(UserPassesTestMixin, CreateView):
    form_class=QuizCreationForm
    template_name='admin.html'
    success_url=reverse_lazy('admin')

    def test_func(self):
        return self.request.user.is_superuser
    
    def no_permission(self):
        raise PermissionError
    
class CategoryCreateView(UserPassesTestMixin, CreateView):
    form_class=CategoryCreationForm
    template_name='admin_Category.html'
    success_url=reverse_lazy('admin_category')

    def test_func(self):
        return self.request.user.is_superuser
    
    def no_permission(self):
        raise PermissionError
    
class LevelCreateView(UserPassesTestMixin, CreateView):
    form_class=LevelCreationForm
    template_name='admin_level.html'
    success_url=reverse_lazy('admin_level')

    def test_func(self):
        return self.request.user.is_superuser
    
    def no_permission(self):
        raise PermissionError