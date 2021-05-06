import requests

for w in [x.strip() for x in open("bruteforce_words.txt").readlines()]:
 if requests.head("https://api.github.com/" + w).status_code != 404:
   print("https://api.github.com/" + w)