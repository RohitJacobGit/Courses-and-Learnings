import requests
from io import BytesIO
from PIL import Image

r = requests.get(
    'https://static.scientificamerican.com/sciam/cache/file/4E0744CD-793A-4EF8-B550B54F7F2C4406.jpg')
print(r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = './image.'+image.format

try:
    image.save(path)
except:
    raise IOError('Cannot save')