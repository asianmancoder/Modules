import requests
import json
import re
# When testing, use this API Key: dc6zaTOxFJmzC
# More functions coming soon!


class Giphy:

    def __init__(self, API_KEY):
        self.base_url = "http://api.giphy.com/v1/gifs/"
        self.api_key_param = "?api_key="
        self.API_KEY = API_KEY

    def trending_gifs(self):
        trending_url = f"{self.base_url}trending{self.api_key_param}{self.API_KEY}"

        data = requests.get(trending_url).json()["data"][0]["url"]
        return data

    def search_gifs(self, query):
        pass

    def random_gif(self):
        pass
