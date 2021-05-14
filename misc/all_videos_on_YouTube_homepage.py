import requests
import re


def ok():
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

  data = requests.get("https://youtube.''' com", headers=headers).text

  vidIDs = [x for x in re.findall('{"videoId":"(.*?)"', data)]
  video_urls = []

  for x in range(0, len(vidIDs), 2):
    video_urls.append(f"https://youtube.com/watch?v={vidIDs[x]}")

  return video_urls
