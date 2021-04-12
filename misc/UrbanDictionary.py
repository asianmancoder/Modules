import requests
import re 


class UrbanDictionary:

  def __init__(self):
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
  
  def definition(self, phrase):
    with requests.session() as s:
      data = s.get(f'https://www.urbandictionary.com/define.php?term={phrase}').text

      definition = re.search('property="fb:app_id"><meta content="(.*?)" name="Description"', data).group(1)
    
    return definition
