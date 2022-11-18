from requests_futures.sessions import FuturesSession
from djangorecipes.settings import dotenv



class TastyCoAPI():
    def __init__(self):
        self.__session = None
        self.__base_url = dotenv.get('TASTYCO_BASE_URL')
        self.__headers = {
            'X-RapidAPI-Key': dotenv.get('TASTYCO_KEY'),
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

    def get_recipes_details(self,params):
        endpoint = "recipes/get-more-info"
        response = self.get(endpoint, params)
        return response.json()

    def get_tips(self,params):
        endpoint = "tips/list"
        response = self.get(endpoint, params)
        if str(response.status_code) == "200":
            return response.json()
        return None

    def get_tags(self,params):
        endpoint = "tags/list"
        response = self.get(endpoint, params)
        return response.json()
    
    def get_feeds(self,params):
        endpoint = "feeds/list"
        response = self.get(endpoint, params)
        return response.json()
    
    def response_hook(self, response):
            return response.json()

    def get(self, endpoint, params):
        if not self.__session:
            self.__session = FuturesSession()

        url = self.__base_url + endpoint
        future = self.__session.request("GET", url, headers = self.__headers, params= params)
        data = future.result()


        return data

client = TastyCoAPI()
