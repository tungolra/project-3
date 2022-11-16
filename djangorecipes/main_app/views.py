from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# for all CBV models
from django.views import generic
from .models import MealPlans, Recipes
from .forms import MealPlanForm, RecipesForm
from . import tc_api
from . import utils

def home(request):
    p = {
        "from" : "938",
        "size" : "12",
    }

    response = tc_api.client.get_recipes_list(p)
    data = utils.parse_recipes_list(response)

    cuisine_tags_values = utils.get_tags_by_type("cuisine", "display_name")

    """
        Usage for getting reviews
    """

    # p_tips = {
    #     "id" : "3562",
    #     "size" : "3"
    # }
    # response_tips = tc_api.client.get_tips(p_tips)
    # reviews = utils.parse_tips(response_tips)
    # # print(reviews)

    """
        Usage for getting similar recipes
    """
    # p_similar = {
    #     "recipe_id" : "3562"
    # }
    # response_similar = tc_api.client.get_recipes_similar(p_similar)
    # data_similar = utils.parse_recipes_similar(response_similar, "s")
    # print(data_similar)

    p_autocomplete = {
        "prefix" : "chicken soup"
    }

    response_autocomplete = tc_api.client.get_recipes_auto_complete(p_autocomplete)
    data_autocomplete = utils.parse_recipes_auto_complete(response_autocomplete)
    print(data_autocomplete)


    for idx, item in enumerate(data):
        if data[idx]['rating']['score']:
            data[idx]['rating']['score'] = round(data[idx]['rating']['score'] * 100, 0)
        data[idx]['rating']['total_count'] = data[idx]['rating']['count_positive'] + data[idx]['rating']['count_negative']
    
    return render(request, 'home.html', {'data': data, 'cuisine_tag_values': cuisine_tags_values})

def example(request):
    p = {
        "from" : "0",
        "size" : "2",
        "tags" : "american"
    }
    
    response = tc_api.client.get_recipes_list(p)
    data = utils.parse_recipes_list(response["results"], "s")

    return render(request, "example.html", {"data" : data} )

"""Meal Plans"""
@login_required
def meal_plan_index(request): 
    meal_plans = MealPlans.objects.filter(user=request.user)
    return render(request, 'meal_plans/index.html', {'meal_plans': meal_plans})

## create Meal Plans
@login_required
def meal_plan_new(request):
    form = MealPlanForm()
    return render(request, 'meal_plans/mealplan_form.html', {'form': form})

@login_required
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
@login_required
def meal_plan_detail(request, mealplan_id):
    meal_plan = MealPlans.objects.get(id=mealplan_id)
    recipes = meal_plan.recipes.all().values()
    recipe_collection = []
    for idx, item in enumerate(recipes): 
        recipe_id = recipes[idx]['recipe_id']
        p = {
        "id":f"{recipe_id}"
        }
        response = tc_api.client.get_recipes_details(p)
        data = utils.parse_recipes_details(response, "d")
        recipe_collection.append(data)
    return render(request, 'meal_plans/detail.html', {'meal_plan': meal_plan, 'recipes': recipes, 'recipe_collection': recipe_collection})

# update Meal Plans
@login_required
def meal_plan_edit(request, mealplan_id):
    """renders page to edit meal plan"""
    meal_plan = MealPlans.objects.get(user=request.user, id=mealplan_id)
    return render(request, 'meal_plans/edit.html', {'meal_plan': meal_plan})

@login_required
def meal_plan_update(request, mealplan_id):
    """updates database"""
    meal_plan = MealPlans.objects.get(user=request.user, id=mealplan_id)
    meal_plan.title = request.POST['name']
    meal_plan.save()
    return redirect(f'/meal-plans/{mealplan_id}/')

# delete Meal Plans
class MealPlanDelete(LoginRequiredMixin, generic.DeleteView):
    model = MealPlans
    success_url = '/meal-plans/'

"""CRUD for Recipes"""

def recipe_index(request): 
    return render(request, 'recipes/index.html')

def add_recipe(request, recipe_id):

    mealplans = MealPlans.objects.filter(user=request.user)
    p = {
        "id":f"{recipe_id}" #REQUIRED
    }
    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipes_details(response, "d")

    return render(request, 'recipes/add.html', {'recipe_id':recipe_id, 'data':data, 'mealplans': mealplans})

def add_recipe_to_meal_plan(request, recipe_id):
    mealplan_id = request.POST['mealplan']
    # add guard for existing recipes in DB
    new_recipe = Recipes.objects.create(recipe_id = recipe_id)
    MealPlans.objects.get(user=request.user, id=mealplan_id).recipes.add(new_recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)

# def recipe_cuisine_index(request): 
#     return render(request, 'recipes/cuisine_index.html')

def recipe_detail(request, recipe_id):
    p = {
        "id":f"{recipe_id}" #REQUIRED
    }
    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipes_details(response, "d")
    return render(request, "recipes/details.html", {"recipe":data})

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




