from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    CHOICES = (
        ('1', 'Choice 1'),
        ('2', 'Choice 2'),
        ('3', 'Choice 3'),
        ('4', 'Choice 4'),
    )

    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    choice_1 = models.CharField(max_length=200)
    choice_2 = models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)
    choice_4 = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=1, choices=CHOICES) 

    def __str__(self):
        return self.question_text
