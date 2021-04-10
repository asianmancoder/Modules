import requests


payload = {
    "content": "hello, I'm sending this using the Discord API!"
}

headers = {
    "Authorization": "NzY4MjgwOTQ4MTU5NTQ1MzY0.YGkLSQ.dQNRReuCw5sy8t5d6UdEOy2dLKo"
}

r = requests.post("https://discord.com/api/v8/channels/818467711436849182/messages", data=payload, headers=headers)
