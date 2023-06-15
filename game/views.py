from django.shortcuts import render

# Create your views here.
def category_view(request):
    # Fetch or create your categories here
    categories = [{"id": 1, "name": "Category 1"}, {"id": 2, "name": "Category 2"}, {"id": 3, "name": "Category 3"}]
    return render(request, 'game/categories.html', {'categories': categories})
def play_view(request, category_id):
    # You would retrieve the particular category and related data here
    # category = Category.objects.get(id=category_id)
    # You would then pass this data to the 'game/play.html' template
    # For now, let's just render an empty template
    return render(request, 'game/play.html')