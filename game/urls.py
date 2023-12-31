from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('categories/', views.category_view, name='categories'),
    path('play/<int:category_id>/', views.play_view, name='play'),
    path('check_answer/', views.check_answer, name='check_answer'),
]