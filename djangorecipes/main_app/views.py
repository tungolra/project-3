from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import MealPlans, Recipes
from .forms import MealPlanForm, RecipesForm
from . import tc_api
from . import utils
import random



def home(request):
    p = {
        "from" : random.randrange(9000),
        "size" : "12",
    }
    response = tc_api.client.get_recipes_list(p)
    data = utils.parse_recipes_list(response)
    tags = utils.get_tags_by_type("cuisine")
    cuisine_tags_values = tags

    for idx, item in enumerate(data):
        if data[idx]['rating']['score']:
            data[idx]['rating']['score'] = round(data[idx]['rating']['score'] * 100, 0)
        data[idx]['rating']['total_count'] = data[idx]['rating']['count_positive'] + data[idx]['rating']['count_negative']
    print(cuisine_tags_values)
    return render(request, 'home.html', {'data': data, 'cuisine_tag_values': cuisine_tags_values})

def cuisine_recipe_list(request, cuisine="american"):
    search_params = {
        "tag" : cuisine,
        "size" : "12",
        "from" : random.randrange(30)
    }
    response = tc_api.client.get_recipes_list(search_params)
    recipes = utils.parse_recipes_list(response)
   
    for idx, item in enumerate(recipes):
        if recipes[idx]['rating']['score']:
            recipes[idx]['rating']['score'] = round(recipes[idx]['rating']['score'] * 100, 0)
        recipes[idx]['rating']['total_count'] = recipes[idx]['rating']['count_positive'] + recipes[idx]['rating']['count_negative']
   
    tag_title = utils.get_tag_by_name(search_params["tag"])["display_name"]

    data = {
        'recipes' : recipes,
        'search_params' : search_params,
        'title' : tag_title
    }

    return render(request, 'recipes/recipe_list.html', data)

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

@login_required
def add_recipe_to_meal_plan(request,recipe_id):
    mealplan_id = request.POST['mealplan']
    mealplan_obj = get_object_or_404(MealPlans, pk=mealplan_id)
    try:
        #Check if mealplan has this recipe
        recipe = mealplan_obj.recipes.get(recipe_id = recipe_id)
        print("Mealplan already has this recipe.")
    except:
        print("Mealplan does not have this recipe!")
        try:
            #Check if recipe exists
            recipe = Recipes.objects.get(recipe_id=recipe_id)
        except:
            recipe = Recipes.objects.create(recipe_id=recipe_id)
        mealplan_obj.recipes.add(recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def delete_recipe_from_meal_plan(request, recipe_id, mealplan_id):
    mealplan = MealPlans.objects.get(pk=mealplan_id)
    recipe = Recipes.objects.get(recipe_id=recipe_id)
    mealplan.recipes.remove(recipe)
    return redirect ('meal_plan_detail', mealplan_id=mealplan_id)

@login_required
def groceries_index(request, mealplan_id):
    def _convert_add(val1, val2):
        return val1 + val2
    recipes = MealPlans.objects.get(pk=mealplan_id).recipes.all().values()
    i_result = {}
    
    for idx, item in enumerate(recipes): 
        recipe_id = recipes[idx]['recipe_id']
        p = {
            "id":f"{recipe_id}"
        }
        response = tc_api.client.get_recipes_details(p)
        data = utils.parse_recipes_details(response, "d")
        ingredients = data['ingredients']
        for ingredient in ingredients:
            i_key = ingredient['name']
            new_val = ingredient.get('quantity')
            i_measurement = i_result.get(i_key)
            if i_measurement:
                i_result[i_key].update({
                    'count': _convert_add(i_measurement['count'], new_val)
                    })
            else: 
                i_result.update({i_key:{
                    'count':new_val, 'unit': ingredient.get('measurement')
                    }})

    return render(request, 'meal_plans/groceries.html', {'ingredients': i_result})

"""CRUD for Recipes"""
@login_required
def toggle_save_recipe(request, recipe_id):
    try:
        print("This recipe is already in the DB!")
        Recipes.objects.get(recipe_id=recipe_id)
    except:
        print("This recipe not included in Recipes DB")
        Recipes.objects.create(recipe_id=recipe_id)
    return redirect('recipe_detail', recipe_id=recipe_id)

def random_recipe(request):
    p = {
    "from" : "0",
    "size" : "20",
    }
    response = tc_api.client.get_recipes_list(p)
    data = utils.parse_recipes_list(response, "s")
    collect_ids = []
    for idx, item in enumerate(data):
        collect_ids.append(data[idx]['id'])
    recipe_id = collect_ids[random.randint(0, len(collect_ids))]
    return recipe_detail(request, recipe_id)

@login_required
def recipe_index(request):
    recipes = Recipes.objects.all().values()
    recipe_collection = []
    for idx, item in enumerate(recipes): 
        recipe_id = recipes[idx]['recipe_id']
        p = {
            "id":f"{recipe_id}"
        }
        response = tc_api.client.get_recipes_details(p)
        data = utils.parse_recipes_details(response, "s")
        recipe_collection.append(data)
    return render(request, 'recipes/index.html', {'recipe_collection': recipe_collection})

@login_required
def add_recipe(request, recipe_id):
    mealplans = MealPlans.objects.filter(user=request.user)
    p = {
        "id":f"{recipe_id}"
    }
    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipes_details(response, "d")

    return render(request, 'recipes/add.html', {'recipe_id':recipe_id, 'data':data, 'mealplans': mealplans})

@login_required
def delete_recipe(request, recipe_id):
    Recipes.objects.filter(recipe_id=recipe_id).delete()
    return redirect("recipe_index")

def recipe_detail(request, recipe_id):
    p = {
        "id":f"{recipe_id}" 
    }
    response = tc_api.client.get_recipes_details(p)
    data = utils.parse_recipes_details(response, "d")
    return render(request, "recipes/details.html", {"recipe":data})

def show_similar_index(request, recipe_id):
    search_params = {
        'recipe_id': recipe_id
    }
    response = tc_api.client.get_recipes_similar(search_params)
    recipes = utils.parse_recipes_list(response)
   
    for idx, item in enumerate(recipes):
        if recipes[idx]['rating']['score']:
            recipes[idx]['rating']['score'] = round(recipes[idx]['rating']['score'] * 100, 0)
        recipes[idx]['rating']['total_count'] = recipes[idx]['rating']['count_positive'] + recipes[idx]['rating']['count_negative']
 
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'title': 'Show me more...' })

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




