import requests
import re
import os


class Downloader:

  def __init__(self, start_page, end_page):
    self.start_page = start_page
    self.end_page = end_page
    self.comic_urls = []
    self.comic_img_urls = []
    self.page_numbers = []
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }

    for x in range(start_page, end_page + 1):
      if requests.get(f"https://xkcd.com/{x}").status_code == 404:
        print(False)

    if start_page >= end_page:
      print(False)

  def get_comic_urls(self):
    self.comic_urls = [f"https://xkcd.com/{x}" for x in range(self.start_page, self.end_page + 1)]
    self.page_numbers = [x for x in range(self.start_page, self.end_page + 1)]

    return self.comic_urls

  def get_comic_img_urls(self):
    self.comic_img_urls = []
    
    try:
      for x in self.get_comic_urls():
        url_src = requests.get(x, headers=self.headers).text
        img_url = "https://" + re.search('<img src="//(.*?)" title=', url_src).group(1)

        self.comic_img_urls.append(img_url)
 
      return self.comic_img_urls
    except: 
      return False

  def download_comics(self):
    os.mkdir("XKCD Comics")

    for num, img in enumerate(self.get_comic_img_urls(), 1):
        with open("XKCD Comics/" + str(num) + ".jpg", "wb") as f:
            img_content = requests.get(img).content
            f.write(img_content)

    return True
