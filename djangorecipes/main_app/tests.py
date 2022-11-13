from django.test import TestCase
from django.urls import reverse
from .models import MealPlans, Recipes

# Create your tests here.

"""Recipe Tests"""

"""Meal Plan Tests"""
class MealPlanIndexTests(TestCase):
    # test if no meal plans exist
    # test if create meal plans are diplayed in the index page
    pass

class MealPlanDetailViewTests(TestCase):
    # detail view of a meal plan returns a 404 not found
    # detail view of a created meal plan displays the meal plan's properties + assoc recipes
    pass

class MealPlanNewTests(TestCase):
    pass

class MealPlanCreateTests(TestCase):
    pass

class MealPlanUpdateTests(TestCase):
    pass

class MealPlanDeleteTests(TestCase):
    pass

"""Grocery Tests"""
