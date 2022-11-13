from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# for all CBV models
from django.views import generic
from .models import MealPlans
from .forms import MealPlanForm
from . import tc_api
from . import utils

"""Recipe Collection"""
def home(request):
    return render(request, 'home.html')

"""Meal Plans"""
# @login_required
def meal_plan_index(request): 
    meal_plans = MealPlans.objects.filter(user=request.user)
    return render(request, 'meal_plans/index.html', {'meal_plans': meal_plans})

# create Meal Plans
# @login_required
def meal_plan_new(request):
    form = MealPlanForm()
    return render(request, 'meal_plans/mealplan_form.html', {'form': form})

# @login_required
def meal_plan_create(request):
    context = {}
    form = MealPlanForm(request.POST)
    if form.is_valid(): 
        form.save(commit=False)
        form.instance.user = request.user
        form.save()
    context['form'] = form
    return redirect('/meal-plans')

# view mealplan details
def meal_plan_detail(request, mealplan_id):
    meal_plan = MealPlans.objects.get(id=mealplan_id)
    return render(request, 'meal_plans/detail.html', {'meal_plan': meal_plan})

# update Meal Plans
# class MealPlanUpdate(generic.UpdateView):
#     model = MealPlans
#     fields = ['title']
def meal_plan_edit(request, mealplan_id):
    meal_plan = MealPlans.objects.get(user=request.user, id=mealplan_id)
    return render(request, 'meal_plans/new.html', {'meal_plan': meal_plan})

def meal_plan_update(request, mealplan_id):
    meal_plan = MealPlans.objects.get(user=request.user, id=mealplan_id)
    meal_plan.title = request.POST['name']
    meal_plan.save()
    return redirect(f'/meal-plans/{mealplan_id}/')

# delete Meal Plans
def delete_collection(request):
    pass

"""CRUD for Recipes"""
# 


"""OAuth Functions"""
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def recipe_view(request):
    p = {
        "recipe_id":"8138" #REQUIRED
    }

    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipe_detail(response["results"][0])
    return render(request, "recipes/details.html", {"recipe":data})


def example(request):
    p = {
        "recipe_id":"8138" #REQUIRED
    }

    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipe_detail(response["results"][0])
    
    return render(request, "example.html", {"data" : data} )
