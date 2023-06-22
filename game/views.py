from django.http import JsonResponse
from django.shortcuts import render
from .models import Game
from questions.models import Question, Category
import random
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def category_view(request):
    # Fetch or create your categories here
    categories = [{"id": 1, "name": "Sports"}, {"id": 2, "name": "Movies/TV"}, {"id": 3, "name": "Music"},{"id": 3, "name": "General Knowledge"}]
    return render(request, 'game/categories.html', {'categories': categories})

def play_view(request, category_id):
    # Retrieve the user and the category
    user = request.user
    category = Category.objects.get(id=category_id)
    game = Game.objects.filter(user=user, category=category).first()

    if game is None:
        game = Game.objects.create(user=user, category=category)

    if game.current_question is None:
        game.current_question = Question.objects.filter(category=category).exclude(id__in=game.questions.all()).order_by('?').first()
        game.save()

    print("Current question:", game.current_question)  # Print the current question

    # Create a list of answer choices for the current question
    question = game.current_question
    choices = [question.choice_1,
               question.choice_2, 
               question.choice_3, 
               question.choice_4]

    return render(request, 'game/play.html', {
    'game': game, 
    'choices': choices,
    'correct_choice_index': game.current_question.correct_choice  # Add this line
})


@login_required
@login_required
@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    answer_id = data.get('answer_id')

    # Retrieve the game instance related to the current user
    game = Game.objects.filter(user=request.user).first()

    if game is None or game.current_question is None:
        # The game does not exist or has no current question
        return JsonResponse({'error': 'Game not found or no question to answer.'}, status=404)

    # Check if the answer is correct
    is_correct = (game.current_question.correct_choice == answer_id)

    # Update the score if the answer is correct
    if is_correct:
        game.score += 10

    # Update the current question
    game.questions.add(game.current_question)
    game.current_question = Question.objects.filter(category=game.category).exclude(id__in=game.questions.all()).order_by('?').first()
    game.save()

    # Create a list of answer choices for the new question
    choices = [game.current_question.choice_1,
               game.current_question.choice_2, 
               game.current_question.choice_3, 
               game.current_question.choice_4]

    # Send back whether the answer was correct, the new question, and choices
    return JsonResponse({'is_correct': is_correct, 'question': game.current_question.question_text, 'choices': choices})
