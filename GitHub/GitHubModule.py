# I utilized the GitHub REST API Data to write this.
# I wrote this comment using the GitHub Web Editor.


import requests

class GitHub:

  def __init__(self):
    self.url = 'https://api.github.com/users/'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
      }

  def information(self, user, select):
    with requests.session() as s:
      APIdata = requests.get(f'{self.url}{user}', headers=self.headers).json()
      
      infoDict = {
        "login": APIdata["login"],
        "avatar": APIdata["avatar_url"],
        "url": APIdata["html_url"],
        "starred": f'https://github.com/{user}?tab=stars',
        "followers": f'{APIdata["followers"]} - https://api.github.com/users/{user}/followers',
        "following": f'{APIdata["following"]} - https://api.github.com/users/{user}/following',
        "repos": f'{APIdata["public_repos"]} - https://github.com/{user}/repositories',
        "name": APIdata["name"],
        "company": APIdata["company"],
        "website": APIdata["blog"],
        "location": APIdata["location"],
        "created": APIdata["created_at"],
        "updated": APIdata["updated_at"]
      }

      if select in infoDict:
        return infoDict[select]
      else: return f'{select} is an invalid key!'


gh = GitHub()
print(gh.information('v1nam'. 'repos'))