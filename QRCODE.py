import qrcode

data = 'MY NAME IS AKSHAY'

img = qrcode.make(data)

img.save('C:/Users/acee/Desktop/QRCODE/myqrcode.png')