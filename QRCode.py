import pyqrcode
import png
from pyqrcode import QRCode

# site = "https://www.google.com/"
site = input("Enter the text/website which you want to make QR : ")
url_qr = pyqrcode.create(site)
name = input("Enter the desired name of you qr : ")
url_qr.svg(name + ".svg", scale=8)
url_qr.png(name + ".png", scale=6)
