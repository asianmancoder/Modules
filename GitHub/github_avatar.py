import requests
import re

#Grabs a GitHub user's avatar

class Avatar:

  def __init__(self):
    self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
    self.theeURL = 'https://github.com/'
    self.avatar = None

  def grabAvatar(self, user):
    with requests.session() as r:
      data = r.get(f'{self.theeURL}{user}', headers=self.headers).text 

      self.avatar = re.search('<meta property="og:image" content="(.*?)"', data).group(1)

    
    
    return self.avatar
