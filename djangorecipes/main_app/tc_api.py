import requests
import environ

env = environ.Env()
environ.Env.read_env()

class TastyCoAPI():
    def __init__(self):
        self.__session = None
        self.__base_url = env('TASTYCO_BASE_URL')
        self.__headers = {
            'X-RapidAPI-Key': env('TASTYCO_KEY'),
            'X-RapidAPI-Host': 'tasty.p.rapidapi.com'
        }
    

    def get_recipes_auto_complete(self, params):
        endpoint = "recipes/auto-complete"
        response = self.get(endpoint, params)

        return response.json()

    def get_recipes_list(self, params):
        endpoint = "recipes/list"
        response = self.get(endpoint, params)

        return response.json()

    def get_recipes_similar(self,params):
        endpoint = "recipes/list-similarities"
        response = self.get(endpoint, params)
        return response.json()

    def get_recipe_detail(self,params):
        endpoint = "recipes/get-more-info"
        response = self.get(endpoint, params)
        return response.json()

    def get_tips(self,params):
        endpoint = "tips/list"
        response = self.get(endpoint, params)
        return response.json()

    def get_tags(self,params):
        endpoint = "tags/list"
        response = self.get(endpoint, params)
        return response.json()
    
    def get_feeds(self,params):
        endpoint = "feeds/list"
        response = self.get(endpoint, params)
        return response.json()
    
    def get(self, endpoint, params):
        url = self.__base_url + endpoint
        response = requests.request("GET", url, headers = self.__headers, params= params)
        return response

client = TastyCoAPI()

'''
    EXAMPLE PARAMETER OBJECTS
client.get_auto_complete(p)
p = { 
    "prefix" : "chicken soup" 
}

client.get_recipes_list(p)
p = { 
    "from" : 5, #REQUIRED
    "size" : 20, #REQUIRED
    "tags" : "under_30_minutes",
    "q" : "food"
}


'''

    
