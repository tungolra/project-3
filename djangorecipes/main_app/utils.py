'''
    Utility file for parsing TastyCo API results
'''
import json
from random import random,randrange
from . import tc_api

# Helper function, parse recipe data from API for detailed views
def helper_recipe_detail(recipe_api: dict) -> dict:
    recipe = helper_nested_recipe(recipe_api)

    result = {
        "id" : helper_get_id(recipe["id"]),
        "name": helper_get_name(recipe["name"]),
        "time": helper_get_time(recipe["cook_time_minutes"]),
        "instructions" : [],
        "ingredients": [],
        "num_servings" : helper_get_num_servings(recipe["num_servings"]),
        "rating" : helper_get_rating(recipe["user_ratings"]), 
        "image_url" : helper_get_image_url(recipe["thumbnail_url"]),
        "image_alt_text" : helper_alt_text(recipe["thumbnail_alt_text"]),
        "video_url" : helper_video_url(recipe["original_video_url"]),
        "nutrition" : helper_nutrition(recipe["nutrition"]),
        # TO ADD,
        # tags
        # Author
    }

    for instruction in recipe["instructions"]:
        result["instructions"].append(helper_instructions(instruction))
    
    for component in recipe["sections"][0]["components"]:
        result["ingredients"].append(helper_ingredient(component))
        
    return result

# Helper function, parse recipe data from API for summary views
def helper_recipe_summary(recipe_api:dict) -> dict:
    recipe = helper_nested_recipe(recipe_api)

    result = {
        "id" : helper_get_id(recipe["id"]),
        "name": helper_get_name(recipe["name"]),
        "time": helper_get_time(recipe["cook_time_minutes"]),
        "num_servings" : helper_get_num_servings(recipe["num_servings"]),
        "rating" : helper_get_rating(recipe["user_ratings"]), 
        "image_url" : helper_get_image_url(recipe["thumbnail_url"]),
        "image_alt_text" : helper_alt_text(recipe["thumbnail_alt_text"]),
        "nutrition" : helper_nutrition(recipe["nutrition"]),
    }

    return result

# Helper for random id if id doesn't exist
def helper_get_id(id):
    if id:
        return id
    return "Missing ID!"

# Helper fill in name if name doesn't exist
def helper_get_name(name):
    if name:
        return name
    return "Tasty! #" + str((randrange(9999)+ 10000))

# Helper for time if time doesn't exist
def helper_get_time(time):
    if time:
        return time
    times = [25, 40 , 55, 60, 75]
    index =randrange(5)
    return times[index]

# Helper for num_servings
def helper_get_num_servings(num):
    if num:
        return num
    servings = [2,4,5,8]
    index =randrange(4)
    return servings[index]

# Helper
def helper_get_rating(rating):
    keys = rating.keys()
    res = {
        'count_positive': rating['count_positive'] or randrange(999),
        'count_negative': rating['count_negative'] or randrange(999),
        'score': rating['score'] or random()
    }
    return res

def helper_get_image_url(url):
    return url

def helper_alt_text(text):
    return text

def helper_video_url(url):
    return url

def helper_nutrition(nutrition):
    return nutrition



# Helper function, parse recipe data if nested in results[i]
def helper_nested_recipe(recipe: dict) -> dict:
    nested = recipe.get("recipes")
    if nested:
        return nested[0]
    return recipe

# Helper function, parse instruction data from API 
def helper_instructions(instruction: dict) -> str:
    res = str(instruction["position"]) + ". " + instruction["display_text"]
    return res

# Helper function, parse ingredients data from APi
def helper_ingredient(recipe_component: dict) -> dict:
    ingredient = recipe_component["ingredient"]

     
    res = {
        "name"  : ingredient["name"],
        "id"    : ingredient["id"],
        "quantity" : "As much as you want of",
        "measurement" : ""

    }

    if len(recipe_component["measurements"]) > 0:
        measurement = recipe_component["measurements"][0]
        res["quantity"] = measurement["quantity"]
        res["measurement"] = measurement["unit"]["abbreviation"]

    return res

# Helper function, parse raw API response and returns relevant data
def helper_response(response: dict) -> dict:
    results = response.get("results")
    if results:
        return results
    else:
        return response

# Parse response from API endpoint, recipes/list
def parse_recipes_list(response: dict, mode:str="s") -> list:
    recipes = helper_response(response)
    print()
    func = None
    
    if mode == "d":
        func = helper_recipe_detail
    elif mode == "s":
        func = helper_recipe_summary
    

    for i in range(len(recipes)):
        recipes[i] = func(recipes[i])
    
    return recipes

# Parse response from API endpoint, recipes/get-more-info
def parse_recipes_details(response: dict, mode: str) -> dict:
    func = None
    
    if mode == "d":
        func = helper_recipe_detail
    elif mode == "s":
        func = helper_recipe_summary

    return func(response)

# Parse response from API endpoint, recipes/autocomplete
def parse_recipes_auto_complete(response: dict) -> dict:
    result = helper_response(response)
    return result[0]

# Parse response from API endpoint, recipes/list-similarities
def parse_recipes_similar(response: dict, mode: str) -> list:
    recipes = helper_response(response)
    func = None
    
    if mode == "d":
        func = helper_recipe_detail
    elif mode == "s":
        func = helper_recipe_summary
    
    for i in range(len(recipes)):
        recipes[i] = func(recipes[i])

    return recipes

# Helper function, parse API tip format for browser
def helper_tip(tip: dict) -> dict:
    tip_result = {
        "text" : tip.get("tip_body"),
        "author_name" : tip.get("author_name"),
        "author_username" : tip.get("author_username"),
        "upvotes" : tip.get("upvotes_total")

    }
    return tip_result

# Parse response from API endpoint, tips/list
def parse_tips(response: dict) -> list:
    tips_list = response.get("results")
    res = []
    for tip in tips_list:
        res += [helper_tip(tip)]
    return res

# Return all tag objects for recipes within the API
def get_all_tags() -> dict:
    with open("./tags", "r") as f:
        tags_dict = json.loads(f.read())
    return tags_dict

# Return all keys for tags within the API
def get_all_tag_types() -> list:
    tags = get_all_tags()
    return tags.keys()

# Get all tags of a specific type
def get_tags_by_type(tag_type: str) -> list:
    tags = get_all_tags()[tag_type]
    return tags
