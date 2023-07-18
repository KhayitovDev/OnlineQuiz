from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Quiz, Category, Level

class QuizCreationForm(forms.ModelForm):

    title = forms.CharField(label='Question Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    option1 = forms.CharField(label='Option1', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    option2 = forms.CharField(label='Option2', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    option3 = forms.CharField(label='Option3', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    option4 = forms.CharField(label='Option4', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
   
    class Meta:
        model=Quiz
        fields='__all__'
        exclude=['user', 'created_at','submitted_at']
        
class CategoryCreationForm(forms.ModelForm):

    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    image = forms.CharField(label='Image url', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model=Category
        fields='__all__'
        
class LevelCreationForm(forms.ModelForm):

    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    image = forms.CharField(label='Image url', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model=Level
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))