#This is a brand - new GitHub written by me!

import requests
import re


class GitHub:

  def __init__(self):
    self.url = 'https://api.github.com/users/'
    self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'}

  def information(self, user, select):
    with requests.session() as s:
      APIdata = requests.get(f'{self.url}{user}', headers=self.headers).json()
      
      if select.lower() == "login":
        return APIdata["login"]
      elif select.lower() == "avatar":
        return APIdata["avatar_url"]
      elif select.lower() == "url":
        return APIdata["html_url"]
      elif select.lower() == "starred":
        return f'https://github.com/{user}?tab=stars'
      elif select.lower() == "followers":
        return f'{APIdata["followers"]} - https://api.github.com/users/asianmancoder/followers'
      elif select.lower() == "following":
        return f'{APIdata["following"]} - https://api.github.com/users/asianmancoder/following'
      elif select.lower() in ("repos", "repo count", "repositories"):
        return f'{APIdata["public_repos"]} - https://github.com/{user}/repositories'
      elif select.lower() == "name":
        return APIdata["name"]
      elif select.lower() == "company":
        return APIdata["company"]
      elif select.lower() == "website":
        return APIdata["blog"]
      elif select.lower() == "location":
        return APIdata["location"]
      elif select.lower() == "bio":
        return APIdata["bio"]
      elif select.lower() == "created":
        return APIdata["created_at"]
      elif select.lower() == "updated":
        return APIdata["updated_at"]

     
if __name__ == "__main__":
  gh = GitHub()
  print(gh.information('v1nam'. 'repo count'))
