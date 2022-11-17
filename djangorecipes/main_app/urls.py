from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('meal-plans/', views.meal_plan_index, name='meal_plan_index'),
    path('meal-plans/new/', views.meal_plan_new, name='meal_plan_new'),
    path('meal-plans/create/', views.meal_plan_create, name='meal_plan_create'),
    path('meal-plans/<int:mealplan_id>/', views.meal_plan_detail, name='meal_plan_detail'),
    path('meal-plans/<int:mealplan_id>/edit', views.meal_plan_edit, name='meal_plan_edit'),
    path('meal-plans/<int:mealplan_id>/submit_update_form', views.meal_plan_update, name='meal_plan_update'),
    path('meal-plans/<int:pk>/delete', views.MealPlanDelete.as_view(), name='meal_plan_delete'),
    path('recipe/<int:recipe_id>/save', views.toggle_save_recipe, name='save_recipe'),
    path('recipe/<int:recipe_id>/add', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/add-to-mealplan/', views.add_recipe_to_meal_plan, name='add_recipe_to_meal_plan'),
    path('recipe/<int:recipe_id>/delete-from-mealplan/<int:mealplan_id>', views.delete_recipe_from_meal_plan, name='delete_recipe_from_meal_plan'),
    path('recipe/index/', views.recipe_index, name="recipe_index"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('recipe/random/', views.random_recipe, name="random_recipe"),
    path('recipe/<int:recipe_id>/delete', views.delete_recipe, name='delete_recipe'),
    path('meal-plans/<int:mealplan_id>/groceries', views.groceries_index, name='groceries_index'),
    path('recipe/recipe_list/<str:cuisine>/', views.cuisine_recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_id>/similar', views.show_similar_index, name="show_similar_index"),

]