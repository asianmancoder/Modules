from io import BytesIO
import requests
from PIL import Image


# A simple way to open an image from the web with PIL without uploading anything from your computer
img_bytes = requests.get("https://i.imgflip.com/2xytmc.jpg").content
bIO_obj = BytesIO(img_bytes)
img = Image.open(bIO_obj)
img.show()
