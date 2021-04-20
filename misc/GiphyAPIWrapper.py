# This is a Giphy API Wrapper for Trending, Search and Random.
# When testing this module, use the example API Key: dc6zaTOxFJmzC
# More functions coming soon.

import requests
import json
import re
import random



class Giphy:

    def __init__(self, API_KEY):
        self.base_url = "http://api.giphy.com/v1/gifs/"
        self.api_key_param = "api_key="
        self.API_KEY = API_KEY
        self.trending_url = f"{self.base_url}trending?{self.api_key_param}{self.API_KEY}"


    def random_trending_gif(self):
        data = requests.get(self.trending_url).json()

        with open("giphyData.txt", "w") as f:
            f.write(str(data))

        with open("giphyData.txt", "r") as f:
            trending_json_data = f.readline()
            giphyURLs = [x for x in re.findall("'url': '(.*?)'", trending_json_data)]

            return random.choice(giphyURLs)


    def first_trending_gif(self):
        data = requests.get(self.trending_url).json()["data"][0]["url"]
        return data


    def search_gifs(self, query):
        pass


    def random_gif(self):
        pass
