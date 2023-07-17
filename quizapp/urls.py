from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'), 
    path('category/<int:pk>/', LevelsListView.as_view(), name='level'),
    path('quizzes/<int:category_id>/level/<int:pk>/', QuizListView.as_view(), name='quizzes'),
    path('leaders/', LeadboardListView.as_view(), name='leaders_board')

]
