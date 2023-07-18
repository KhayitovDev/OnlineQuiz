from django.urls import path
from .views import *

urlpatterns = [
     #user authentication urls
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    #--------------------------------------------------------#
    path('', CategoryListView.as_view(), name='category'), 
    path('category/<int:pk>/', LevelsListView.as_view(), name='level'),
    path('quizzes/<int:category_id>/level/<int:pk>/', QuizListView.as_view(), name='quizzes'),
    path('leaders/<int:category_id>/<int:pk>/', LeadboardListView.as_view(), name='leaders_board'),

    #--------------------------------------------#
    path('admin_page/', QuizCreateView.as_view(), name='admin'),
    path('admin_category/', CategoryCreateView.as_view(), name='admin_category'),
    path('admin_level/', LevelCreateView.as_view(), name='admin_level'),

]
