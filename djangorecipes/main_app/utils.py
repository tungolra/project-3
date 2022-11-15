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
    measurement = recipe_component["measurements"][0]

    res = {
        "name"  : ingredient["name"],
        "id"    : ingredient["id"],
        "quantity"  : measurement["quantity"],
        "measurement" : measurement["unit"]["abbreviation"]
    }

    return res

# Helper function, parse raw API response and returns relevant data
def helper_response(response: dict) -> dict:
    result = response.get("results")
    if result:
        return result
    else:
        return response

# Parse response from API endpoint, recipes/list
def parse_recipes_list(recipes: dict, mode:str="s") -> list:
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
def parse_recipes_auto_complete(response: dict, mode: str) -> dict:
    result = helper_response(response)

    return result[0]

# TODO
# Parse response from API endpoint, recipes/list-similarities
def parse_recipes_similar(response: dict, mode: str) -> list:
    pass

# TODO
# Parse response from API endpoint, tips/list
def parse_tips(response: dict,mode: str) -> list:
    pass

# Return all tag objects for recipes within the API
def get_all_tags() -> dict:
    with open("tags.txt", "r") as f:
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
