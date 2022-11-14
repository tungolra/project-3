'''
    Utility file for parsing TastyCo API results
'''

from . import tc_api

def parse_recipe_detail(recipe):
    result = {
        "id" : recipe["id"],
        "name": recipe["name"],
        "instructions" : [],
        "ingredients": [],
        "num_servings" : recipe["num_servings"],
        "rating" : recipe["user_ratings"], 
        "image_url" : recipe["thumbnail_url"],
        "image_alt_text" : recipe["thumbnail_alt_text"],
        "video_url" : recipe["original_video_url"],
        "nutrition" : recipe["nutrition"]
        # TO ADD,
        # Ingredients,
        # Cook Time
        # Author
    }

    for instruction in recipe["instructions"]:
        result["instructions"].append(parse_instruction(instruction))
    

    for component in recipe["sections"][0]["components"]:
        result["ingredients"].append(parse_ingredient(component))
        
    return result


def parse_recipe_summary(recipe):
    result = {
        "id" : recipe["id"],
        "name": recipe["name"],
        "num_servings" : recipe["num_servings"],
        "rating" : recipe["user_ratings"], 
        "image_url" : recipe["thumbnail_url"],
        "image_alt_text" : recipe["thumbnail_alt_text"],
        "nutrition" : recipe["nutrition"]
    }

    return result

def parse_instruction(instruction):
    res = str(instruction["position"]) + " " + instruction["display_text"]
    return res

def parse_ingredient(recipe_component):
    ingredient = recipe_component["ingredient"]
    measurement = recipe_component["measurements"][0]

    res = {
        "name"  : ingredient["name"],
        "id"    : ingredient["id"],
        "quantity"  : measurement["quantity"],
        "measurement" : measurement["unit"]["abbreviation"]
    }
    return res

def parse_response(response):
    result = response.get("results")
    if result:
        return result
    else:
        return response

def parse_recipes_list(recipes, mode="s"):
    func = None
    
    if mode == "d":
        func = parse_recipe_detail
    elif mode == "s":
        func = parse_recipe_summary
    

    for i in range(len(recipes)):
        recipes[i] = func(recipes[i])
    
    return recipes

def parse_recipes_auto_complete(response, mode):
    result = parse_response(response)

    return result[0]

def parse_recipes_similar(response, mode):
    pass

def parse_recipes_details(response, mode):
    func = None
    
    if mode == "d":
        func = parse_recipe_detail
    elif mode == "s":
        func = parse_recipe_summary

    return func(response)

def parse_tips(response,mode):
    pass

def parse_tags(response, mode):
    pass

def parse_feeds(responsee, mode):
    pass





if __name__ == "__main__":
    p = {
        "recipe_id":"8138" #REQUIRED
    }

    recipe = tc_api.client.get_recipes_details(p)

    data = parse_recipe_detail(recipe)
    print(data)

