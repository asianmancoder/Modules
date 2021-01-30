import requests
import re

#Grabs a GitHub user's username

class Username:

  def __init__(self):
    self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
    self.theeURL = 'https://github.com/'
    self.username = None
  
  def grabUsername(self, user):
    with requests.session() as s:
      data = s.get(f'{self.theeURL}{user}', headers=self.headers).text

      self.avatar = re.search('<title>(.*?)</title>', data).group(1)

    return 
    
    self.avatar
