from django.shortcuts import render
from .models import Game
from questions.models import Question, Category
import random
# Create your views here.
def category_view(request):
    # Fetch or create your categories here
    categories = [{"id": 1, "name": "Sports"}, {"id": 2, "name": "Movies/TV"}, {"id": 3, "name": "Music"},{"id": 3, "name": "General Knowledge"}]
    return render(request, 'game/categories.html', {'categories': categories})

def play_view(request, category_id):
    # Retrieve the user and the category
    user = request.user
    category = Category.objects.get(id=category_id)

    # Try to get an existing game for this user and category
    game = Game.objects.filter(user=user, category=category).first()

    if game is None:
        # If there is no existing game, create a new one
        game = Game.objects.create(user=user, category=category)

    # If there is no current question, get the first question from the category
    if game.current_question is None:
        game.current_question = Question.objects.filter(category=category).exclude(id__in=game.questions.all()).order_by('?').first()
        game.save()

    print("Current question:", game.current_question)  # Print the current question

    # Pass the game to the template
    return render(request, 'game/play.html', {'game': game})

