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
    # test if HTTP request renders page to create a new meal plan
    pass

class MealPlanCreateTests(TestCase):
    # test if invalid entry in form does not create new meal plan when submitted
    # test if valid entry in form creates new meal plan when submitted
    pass

class MealPlanEditTests(TestCase):
    # returns 404 for invalid redirect of selected meal plan
    # test if HTTP request renders page to update a new meal plan
    pass

class MealPlanUpdateTests(TestCase):
    # test if invalid entry in form does not update meal plan when submitted
    # test if valid entry in form creates new meal plan when submitted
    pass

class MealPlanDeleteTests(TestCase):
    # test if page redirects to meal plan index after submitting delete form
    # test if document is removed from database upon submission of delete form
    pass

"""Grocery Tests"""
