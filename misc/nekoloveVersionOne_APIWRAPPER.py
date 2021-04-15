import requests


def nekoGet(endpoint):

    try: 
        neko_endpoints = ["neko", "nekolewd", "kitsune", "pat", "hug", "waifu", "cry", "kiss", "slap", "smug", "punch"]

        if endpoint not in neko_endpoints:
            return "Endpoint not found."
        
        data = requests.get(f"https://neko-love.xyz/api/v1/{endpoint}").json()["url"]

        return data
    except Exception as e:
        return e
