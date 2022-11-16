'''
    Utility file for parsing TastyCo API results
'''
import json
from . import tc_api

# Helper function, parse recipe data from API for detailed views
def helper_recipe_detail(recipe_api: dict) -> dict:
    recipe = helper_nested_recipe(recipe_api)

    result = {
        "id" : recipe["id"],
        "name": recipe["name"],
        "time": recipe["cook_time_minutes"],
        "instructions" : [],
        "ingredients": [],
        "num_servings" : recipe["num_servings"],
        "rating" : recipe["user_ratings"], 
        "image_url" : recipe["thumbnail_url"],
        "image_alt_text" : recipe["thumbnail_alt_text"],
        "video_url" : recipe["original_video_url"],
        "nutrition" : recipe["nutrition"],
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
        "id" : recipe["id"],
        "name": recipe["name"],
        "time": recipe["cook_time_minutes"],
        "num_servings" : recipe["num_servings"],
        "rating" : recipe["user_ratings"], 
        "image_url" : recipe["thumbnail_url"],
        "image_alt_text" : recipe["thumbnail_alt_text"],
        "nutrition" : recipe["nutrition"]
    }

    return result

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
        "quantity" : "You decide!",
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
def get_tags_by_type(tag_type: str, value: str) -> list:
    tags = get_all_tags()[tag_type]

    res = []
    for tag in tags:
        res += [tag[value]]
    return res
