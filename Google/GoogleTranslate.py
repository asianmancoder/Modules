import requests
import re


class Google:
  
  def __init__(self):
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    self.SearchUrl = 'https://google.com/search?q='
    self.GoogleTrans = 'google translate'
  
  def GTranslate(self, phrase):
    with requests.session() as s:
        data = s.get(f'{self.SearchUrl}{self.GoogleTrans}{phrase}', headers=self.headers).text

        translated = re.search('<pre class="tw-data-text tw-text-large XcVN5d tw-ta" data-placeholder="Translation" id="tw-target-text" style="text-align:left"><span>(.*?)</span>', data).group(1)
        lang = re.search('<span class="source-language">(.*?) - detected</span>', data).group(1)
    
    infoDict = {
        "Query": phrase,
        "Detected Language": lang,
        "Translation": translated
    }

    return infoDict
