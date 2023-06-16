from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Question
from random import shuffle

def category_view(request, category_name):
    print(category_name)  # this line is for debugging, you can remove it later
    # Retrieve the category object based on the name passed in the URL
    category = get_object_or_404(Category, name=category_name)
    
    # Retrieve all questions for this category
    questions = list(Question.objects.filter(category=category))
    
    # Shuffle the questions to provide a different experience each time
    shuffle(questions)
    
    # Limit to 20 questions
    questions = questions[:20]

    context = {
        'category': category,
        'questions': questions,
    }

    return render(request, 'questions/category.html', context)

def test_view(request):
    return HttpResponse('This is a test.')
