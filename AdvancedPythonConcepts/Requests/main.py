import requests
from io import BytesIO
from PIL import Image

r = requests.get('https://wallpapercave.com/wp/Jzn5hwl.jpg')
print('Status Code:', r.status_code)

image = Image.open(BytesIO(r.content)) # Using BytesIO because it is Binary Data

print(image.size, image.format, image.mode)
path = 'image.' + image.format

try:
    image.save(path, image.format)
except IOError:
    print('Cannot save Image')