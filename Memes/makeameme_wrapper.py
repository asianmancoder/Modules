import requests
import re

# LOL
# This is an unfinished program

class MakeMeme:

  def __init__(self):
    self.headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    self.meme_ids = {
      "Among Us": 553,
      "Happy Squirrel": 187 
    }

  def create(self, template, top, bottom):
    if template not in list(self.meme_ids):
      return 'Invalid Template!'

    meme_data = {
      "meme": self.meme_ids[template],
      "top-text": top,
      "bottom-text": bottom,
      "title-text": "CUSTOM MEME",
      "memeIsVisible": 1
    }

    with requests.session() as MEME:
      meme = MEME.post('https://makeameme.org/ajax/createMeme.php', data=meme_data, headers=self.headers).text

      actual_meme = re.search('<meta property="og:image" content="(.*?)" />', meme).group(1)

      return actual_meme
