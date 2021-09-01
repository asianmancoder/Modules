import json


class Filters:

  def __init__(self, guild_id):
    with open("filter_file.json", "r") as f:
      self.filter_data = json.loads(f.read())
    
    self.guild_id = guild_id

  def save(self):
    with open("filter_file.json", "w") as f:
      f.write(json.dumps(self.filter_data))

  def add_guild(self, guild_id):
    self.filter_data[guild_id] = {}
    self.save()

  def delete_guild(self, guild_id):
    if not self.filter_data[guild_id]:
      return f"Guild {guild_id} does not exist."
    else:
      del self.filter_data[guild_id]
      self.save()

  def add_filter(self, guild_id, trigger, response):
    if not self.filter_data[guild_id]:
      return f"Guild {guild_id} does not exist."
    else:
      self.filter_data[guild_id][trigger] = response
      self.save()

  def delete_filter(self, guild_id, trigger):
    if not self.filter_data[guild_id][trigger]:
      return f"Trigger {trigger} not found."
    else:
      del self.filter_data[guild_id][trigger]
      self.save()
  
  def do_filter(self, guild_id, trigger):
    if not self.filter_data[guild_id][trigger]:
      return f"Trigger {trigger} not found."
    else:
      return self.filter_data[guild_id][trigger]

  def contains(self, message, s):
    if s in message:
      return True
    else:
      return False

  def check_message(self, message, guild_id):
    for trigger in self.filter_data[guild_id]:
      if self.contains(trigger, message):
        return self.filter_data[guild_id][trigger]
