from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('meal-plans', views.meal_plan_index, name='meal_plan_index'),
    path('meal-plans/new', views.meal_plan_new, name='meal_plan_new'),
    path('meal-plans/create', views.meal_plan_create, name='meal_plan_create'),
    path('recipe', views.recipe_view, name="recipe_view"),
    path('example', views.example, name="example"),
]