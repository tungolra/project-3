from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

class Recipes(models.Model):
    recipe_id = models.IntegerField()



class MealPlans(models.Model):
    title = models.CharField(max_length=50)

    recipes = models.ManyToManyField(Recipes)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('details', kwargs={'mealplan_id': self.id})
