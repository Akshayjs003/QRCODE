import qrcode

data = 'GIVE ANY DATA'

img = qrcode.make(data)

img.save('C:/Users/acee/Desktop/QRCODE/myqrcode.png')
