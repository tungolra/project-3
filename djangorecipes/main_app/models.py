from django.db import models
from django.urls import reverse # used for update/create redirects
from django.contrib.auth.models import User

class Recipes(models.Model):
    # for API only; create own recipe TBD
    recipe_id = models.IntegerField()
    def __str__(self): 
        return self.id


class RecipeCollection(models.Model):
    title = models.CharField(max_length=50)

    recipes = models.ManyToManyField(Recipes)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Collection Name: {self.title}'

    def get_absolute_url(self):
        return reverse('index')


# class Photos 

# class GroceryList
