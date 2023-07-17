from django.contrib import admin
from .models import Category, Quiz, UserAnswer,Level

# Register your models here.

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(UserAnswer)
admin.site.register(Level)