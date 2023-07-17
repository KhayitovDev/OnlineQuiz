from typing import Any, Dict
from django.db import models
from random import shuffle
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Quiz, Category, Level, UserAnswer
from django.db.models import Q
# Create your views here.


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

class QuizListView(ListView):
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
            'user':user
        }

        return render(request, 'result.html', {'result': result})

class LeadboardListView(ListView):
    template_name = 'leaderboard.html'
    context_object_name = 'leaders'

    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        level_id = self.request.GET.get('level_id')

        queryset = UserAnswer.objects.all()

        if category_id and level_id:
            queryset = queryset.filter(category_id=category_id, level_id=level_id)
        elif category_id:
            queryset = queryset.filter(category_id=category_id)
        elif level_id:
            queryset = queryset.filter(level_id=level_id)

        queryset = queryset.order_by('-score')
        return queryset
