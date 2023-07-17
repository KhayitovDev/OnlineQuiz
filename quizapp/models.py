from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title
    
    
class Level(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    CORRECT_ANSWER_CHOICES = [
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3', 'option3'),
        ('option4', 'option4'),
      
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    levels=models.ForeignKey(Level, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    option1=models.CharField(max_length=250)
    option2=models.CharField(max_length=250)
    option3=models.CharField(max_length=250)
    option4=models.CharField(max_length=250)
    correct_answers=models.CharField(max_length=250, choices=CORRECT_ANSWER_CHOICES,  null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    submitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class UserAnswer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    level=models.ForeignKey(Level, on_delete=models.CASCADE)
    score=models.IntegerField()


    def __str__(self):
        return f"{self.user.username}- {self.score}"
    
    
    

