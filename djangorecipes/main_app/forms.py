from django.forms import ModelForm
from .models import MealPlans, Recipes

class MealPlanForm(ModelForm):
    class Meta: 
        model = MealPlans
        fields = ['title']

class RecipesForm(ModelForm):
    class Meta: 
        model = Recipes
        fields = ['recipe_id']