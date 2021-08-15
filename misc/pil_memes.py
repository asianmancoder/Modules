from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont


def meme(text):
    img_bytes = requests.get("https://i.imgflip.com/2xytmc.jpg").content
    bIO_obj = BytesIO(img_bytes)

    with Image.open(bIO_obj) as img:
        width, height = img.size
        draw = ImageDraw.Draw(img)
        draw.text(((width/2) - 450, (height/2) + 300), text, font=ImageFont.truetype("arial.ttf", 30), fill=(0, 0, 0))
        img.show()
