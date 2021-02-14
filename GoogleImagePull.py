import requests
import re
import random


def image(*image_query):
  with requests.session() as s:
    image_query = " ".join(image_query)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    data = s.get(f'https://www.google.com/search?q={image_query}&tbm=isch', headers=headers).text
    
    image = [x.group(1) for x in re.finditer(r'(https?://.*?\.(png|jpg|gif))(",\d{3,4},\d{3,4})', data)]
    
    while 1 == 1:
      return random.choice(image)
      break
