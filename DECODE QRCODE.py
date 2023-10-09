from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/acee/Desktop/QRCODE/myqrcode.png')

result = decode(img)

print(result)