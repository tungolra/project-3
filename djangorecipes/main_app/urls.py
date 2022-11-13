from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('meal-plans', views.meal_plan_index, name='meal_plan_index'),
    path('collections/create', views.MealPlanCreate.as_view(), name='recipe_collection_create'),
]