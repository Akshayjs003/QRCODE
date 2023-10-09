import qrcode

data = 'MY NAME IS AKSHAY'

qr = qrcode.QRCode(version = 1, box_size =10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'black')

img.save('C:/Users/acee/Desktop/QRCODE/myqrcode1.png')