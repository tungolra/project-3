from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.recipe_collection_index, name='recipe_collection_index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipe', views.recipe_view, name="recipe_view"),
    path('example', views.example, name="example")
]