import requests
import re 

#Grabs the first result from a query on YouTube - Surprisingly simple!!

class YouTube: 

  def __init__(self): 
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"} 

  def debugger(self, data): 
    with open('debugYTData.txt', 'w', encoding="UTF-8") as y: 
      y.write(data) 
      
  def video(self, query): 
    with requests.session() as s: 
      d = s.get(f'https://youtube.com/results?search_query={query}', headers=self.headers).text 

      vidID = re.search('{"videoId":"(.*?)","thumbnail"', d).group(1) 
      
      return f'https://youtube.com/watch?v={vidID}' 
