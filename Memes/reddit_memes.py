import requests
import re

#Grabs random meme from r/memes from Reddit

class Reddit:

  def __init__(self):
    self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
  
  def theeMeme(self):
    with requests.session() as s:
      data = s.get('https://reddit.com/r/memes/random/.json', headers=self.headers).json()[0]['data']['children'][0]['data']

      theeMeme = {
        'A meme from r/memes: ': data['title'],
        'URL: ': data['url']
      }

      sortedMemes = sorted(theeMeme.items(), key=lambda x: x[1])

    return ("\n".join([f'{key}: {value}'for key, value in sortedMemes]))
