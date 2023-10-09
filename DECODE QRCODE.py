from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('LOCATION OF YOUR QRCODE')

result = decode(img)

print(result)
