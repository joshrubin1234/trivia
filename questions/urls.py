from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('<str:category_name>/', views.category_view, name='category_view'),
]
