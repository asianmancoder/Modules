import requests
import re

#Grabs a random fact from https://randomfactgenerator.net/

class Fact:

  def __init__(self):
    self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}

  def grabFact(self):
    return re.search('<div id=\'z\'>(.*?).<br/><br/>',
           requests.get('http://randomfactgenerator.net/').text).group(1)
