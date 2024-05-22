import os
import qrcode
from PIL import Image
n=input()
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)  # Generate QR code with various customization
qr.add_data(n)
qr.make(fit=True)
img=qr.make_image(fill_colr="black",back_color="white")
img.save("QRCodeAb.png")
os.system("open QRCodeAb.png")