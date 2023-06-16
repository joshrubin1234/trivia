from django.db import models
from django.contrib.auth.models import User
from questions.models import Category, Question

# Create your models here.

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='+')
