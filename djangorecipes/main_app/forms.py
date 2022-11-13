from django.forms import ModelForm
from .models import MealPlans

class MealPlanForm(ModelForm):
    class Meta: 
        model = MealPlans
        fields = ['title']