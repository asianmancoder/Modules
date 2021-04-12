import requests
import re
import random


class Imgur:

  def __init__(self):
    self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

  def debug(self, d):
    with open('debugger.txt', 'w') as f:
      f.write(str(d))

  def get_rand_result(self, query):
    query = " ".join(query)
    with requests.session() as s:
      data = s.get(f'https://imgur.com/search?q={query}', headers=self.headers).text

      image_container = [img.split('<img alt="" src="//')[-1].split('" />')[0] for img in re.findall('<img alt="" src="//(.*?)" />', data) if img.endswith('.jpg') or img.endswith('.png') or img.endswith('.gif')]
      
      return random.choice(image_container)
