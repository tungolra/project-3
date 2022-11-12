'''
    Utility file for parsing TastyCo API results
'''
from . import tc_api

def parse_recipe_detail(response):
    recipe = response["results"][0]
    result = {
        "id" : recipe["id"],
        "name": recipe["show"]["name"],
        "instructions" : [],
        "num_servings" : recipe["num_servings"],
        "rating" : recipe["user_ratings"], 
        "image_url" : recipe["thumbnail_url"],
        "image_alt_text" : recipe["thumbnail_alt_text"],
        "video_url" : recipe["original_video_url"],
        "nutrition" : recipe["nutrition"]
    }

    for instruction in recipe["instructions"]:
        result["instructions"].append(parse_instruction(instruction))

    print(result)
    return result

def parse_recipe_summary(recipe):
    pass

def parse_instruction(instruction):
    res = str(instruction["position"]) + " " + instruction["display_text"]
    return res


if __name__ == "__main__":
    p = {
        "recipe_id":"8138" #REQUIRED
    }

    recipe = tc_api.client.get_recipes_details(p)

    data = parse_recipe_detail(recipe)
    print(data)