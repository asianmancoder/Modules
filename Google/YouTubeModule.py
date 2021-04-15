import requests
import re



class YouTube:

    def __init__(self, videoQuery):
        self.base_query_url = "https://youtube.com/"
        self.base_watch_url = None # Not accomplished yet.
