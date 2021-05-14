import json


class Filters:

  def __init__(self):
    with open('filter_file.json', 'r') as f:
      self.filter_data = json.loads(f.read())

  def save(self):
    with open('filter_file.json', 'w') as f:
      f.write(json.dumps(self.filter_data))

  def filter_add(self, trigger, response):
    self.filter_data[trigger] = response
    self.save()
    return "Done"

  def filter_do(self, trigger):
    return self.filter_data[trigger]
